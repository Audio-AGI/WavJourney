import datetime
import os
from string import Template
import openai
import re
import glob
import pickle
import time
import json5
from retrying import retry
from code_generator import check_json_script, collect_and_check_audio_data
import random
import string

import utils
import voice_presets
from code_generator import AudioCodeGenerator

# Enable this for debugging
USE_OPENAI_CACHE = False
openai_cache = []
if USE_OPENAI_CACHE:
    os.makedirs('cache', exist_ok=True)
    for cache_file in glob.glob('cache/*.pkl'):
        with open(cache_file, 'rb') as file:
            openai_cache.append(pickle.load(file))

def chat_with_gpt(prompt, api_key):
    if USE_OPENAI_CACHE:
        filtered_object = list(filter(lambda x: x['prompt'] == prompt, openai_cache))
        if len(filtered_object) > 0:
            response = filtered_object[0]['response']
            return response
    
    try:
        openai.api_key = api_key
        chat = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo",
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    finally:
        openai.api_key = ''

    if USE_OPENAI_CACHE:
        cache_obj = {
            'prompt': prompt,
            'response': chat['choices'][0]['message']['content']
        }
        with open(f'cache/{time.time()}.pkl', 'wb') as _openai_cache:
            pickle.dump(cache_obj, _openai_cache)
            openai_cache.append(cache_obj)

    return chat['choices'][0]['message']['content']


def get_file_content(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def extract_substring_with_quotes(input_string, quotes="'''"):
    pattern = f"{quotes}(.*?){quotes}"
    matches = re.findall(pattern, input_string, re.DOTALL)
    return matches


def try_extract_content_from_quotes(content):
    if "'''" in content:
        return extract_substring_with_quotes(content)[0]
    elif "```" in content:
        return extract_substring_with_quotes(content, quotes="```")[0]
    else:
        return content

def maybe_get_content_from_file(content_or_filename):
    if os.path.exists(content_or_filename):
        with open(content_or_filename, 'r') as file:
            return file.read().strip()
    return content_or_filename



# Pipeline Interface Guidelines:
#
# Init calls:
# - Init calls must be called before running the actual steps
#   - init_session() is called every time a gradio webpage is loaded
#
# Single Step:
# - takes input (file or content) and output path as input
# - most of time just returns output content
# 
# Compositional Step:
# - takes session_id as input (you have session_id, you have all the paths)
# - run a series of steps

# This is called for every new gradio webpage

def init_session(session_id=''):
    def uid8():
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    if session_id == '':
        session_id = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}_{uid8()}'
    # create the paths
    os.makedirs(utils.get_session_voice_preset_path(session_id))
    os.makedirs(utils.get_session_audio_path(session_id))
    print(f'New session created, session_id={session_id}')
    return session_id

@retry(stop_max_attempt_number=3)
def input_text_to_json_script_with_retry(complete_prompt_path, api_key):
    print("    trying ...")
    complete_prompt = get_file_content(complete_prompt_path)
    json_response = try_extract_content_from_quotes(chat_with_gpt(complete_prompt, api_key))
    json_data = json5.loads(json_response)

    try:
        check_json_script(json_data)
        collect_and_check_audio_data(json_data)
    except Exception as err:
        print(f'JSON ERROR: {err}')
        retry_complete_prompt = f'{complete_prompt}\n```\n{json_response}```\nThe script above has format error(s). Return the fixed script.\n\nScript:\n'
        write_to_file(complete_prompt_path, retry_complete_prompt)
        raise err

    return json_response

# Step 1: input_text to json
def input_text_to_json_script(input_text, output_path, api_key):
    input_text = maybe_get_content_from_file(input_text)
    text_to_audio_script_prompt = get_file_content('prompts/text_to_json.prompt')
    prompt = f'{text_to_audio_script_prompt}\n\nInput text: {input_text}\n\nScript:\n'
    complete_prompt_path = output_path / 'complete_input_text_to_audio_script.prompt'
    write_to_file(complete_prompt_path, prompt)
    audio_script_response = input_text_to_json_script_with_retry(complete_prompt_path, api_key)
    generated_audio_script_filename = output_path / 'audio_script.json'
    write_to_file(generated_audio_script_filename, audio_script_response)
    return audio_script_response

# Step 2: json to char-voice map
def json_script_to_char_voice_map(json_script, voices, output_path, api_key):
    json_script_content = maybe_get_content_from_file(json_script)
    prompt = get_file_content('prompts/audio_script_to_character_voice_map.prompt')
    presets_str = '\n'.join(f"{preset['id']}: {preset['desc']}" for preset in voices.values())
    prompt = Template(prompt).substitute(voice_and_desc=presets_str)
    prompt = f"{prompt}\n\nAudio script:\n'''\n{json_script_content}\n'''\n\noutput:\n"
    write_to_file(output_path / 'complete_audio_script_to_char_voice_map.prompt', prompt)
    char_voice_map_response = try_extract_content_from_quotes(chat_with_gpt(prompt, api_key))
    char_voice_map = json5.loads(char_voice_map_response)
    # enrich char_voice_map with voice preset metadata
    complete_char_voice_map = {c: voices[char_voice_map[c]] for c in char_voice_map}
    char_voice_map_filename = output_path / 'character_voice_map.json'
    write_to_file(char_voice_map_filename, json5.dumps(complete_char_voice_map))
    return complete_char_voice_map
    
# Step 3: json to py code
def json_script_and_char_voice_map_to_audio_gen_code(json_script_filename, char_voice_map_filename, output_path, result_filename):
    audio_code_generator = AudioCodeGenerator()
    code = audio_code_generator.parse_and_generate(
        json_script_filename,
        char_voice_map_filename,
        output_path,
        result_filename
    )
    write_to_file(output_path / 'audio_generation.py', code)

# Step 4: py code to final wav
def audio_code_gen_to_result(audio_gen_code_path):
    audio_gen_code_filename = audio_gen_code_path / 'audio_generation.py'
    os.system(f'PYTHONPATH=. python {audio_gen_code_filename}')

# Function call used by Gradio: input_text to json
def generate_json_file(session_id, input_text, api_key):
    output_path = utils.get_session_path(session_id)
    # Step 1
    print(f'session_id={session_id}, Step 1: Writing audio script with LLM ...')
    return input_text_to_json_script(input_text, output_path, api_key)

# Function call used by Gradio: json to result wav
def generate_audio(session_id, json_script, api_key):
    def count_lines(content):
        # Split the string using the newline character and count the non-empty lines
        return sum(1 for line in content.split('\n') if line.strip())

    max_lines = utils.get_max_script_lines()
    if count_lines(json_script) > max_lines:
        raise ValueError(f'The number of lines of the JSON script has exceeded {max_lines}!')

    output_path = utils.get_session_path(session_id)
    output_audio_path = utils.get_session_audio_path(session_id)
    voices = voice_presets.get_merged_voice_presets(session_id)

    # Step 2
    print(f'session_id={session_id}, Step 2: Parsing character voice with LLM...')
    char_voice_map = json_script_to_char_voice_map(json_script, voices, output_path, api_key)
    # Step 3
    json_script_filename = output_path / 'audio_script.json'
    char_voice_map_filename = output_path / 'character_voice_map.json'
    result_wav_basename = f'res_{session_id}'
    print(f'session_id={session_id}, Step 3: Compiling audio script to Python program ...')
    json_script_and_char_voice_map_to_audio_gen_code(json_script_filename, char_voice_map_filename, output_path, result_wav_basename)
    # Step 4
    print(f'session_id={session_id}, Step 4: Start running Python program ...')
    audio_code_gen_to_result(output_path)

    result_wav_filename = output_audio_path / f'{result_wav_basename}.wav'
    print(f'Done all processes, result: {result_wav_filename}')
    return result_wav_filename, char_voice_map

# Convenient function call used by wavjourney_cli
def full_steps(session_id, input_text, api_key):
    json_script = generate_json_file(session_id, input_text, api_key)
    return generate_audio(session_id, json_script, api_key)
