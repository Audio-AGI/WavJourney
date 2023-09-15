import os
import sys
sys.path.append('../WavJourney')
import csv
import json
from pathlib import Path
import pipeline
import voice_presets

voices = voice_presets.load_voice_presets_metadata(voice_presets_path='/home/lxb/Disk_SSD/WavJourney/data/voice_presets')

def generate_script(input_text, output_path, api_key, basename):
    # step 1
    json_script = pipeline.input_text_to_json_script(input_text, output_path, api_key)
    print('Step 1 completed.')
    # step 2
    char_voice_map = pipeline.json_script_to_char_voice_map(json_script, voices, output_path, api_key)
    print('Step 2 completed.')
    # step 3
    json_script_filename = output_path / 'audio_script.json'
    char_voice_map_filename = output_path / 'character_voice_map.json'
    
    result_wav_basename = f'{basename}'
    pipeline.json_script_and_char_voice_map_to_audio_gen_code(json_script_filename, char_voice_map_filename, output_path, result_wav_basename)
    print('Step 3 completed.')



if __name__ == '__main__':
    json_path = '/home/lxb/Disk_SSD/WavJourney/ICLR/audiocaps.json'
    output_dir = 'ICLR/AudioCaps'
    api_key = ''

    prompt = '(overall length must be 10 seconds)'

    err_path = '/home/lxb/Disk_SSD/WavJourney/ICLR/audiocaps_err.json'
    err_meta = []

    with open(json_path, 'r') as file:
        # Read each line and parse it as JSON
        for id, line in enumerate(file):
            data = json.loads(line)
            caption = data["caption"]
            wav_name = data["name"]
            basename = wav_name[:-4]

            metadata = f'{wav_name}, {caption}'

            # create folder
            output_path = os.path.join(output_dir, basename)
            os.makedirs(output_path, exist_ok=True)

            with open(os.path.join(output_path, 'metadata.txt'), 'w') as file:
                file.write(metadata)

            input_text = caption + ' ' + prompt

            try:
                print(f'Example [{id}] starts | {caption}')

                generate_script(
                    input_text, 
                    Path(output_path), 
                    api_key, 
                    basename
                )

                err_dict = {'caption': caption, 'name': wav_name}

                err_meta.append(err_dict)

            except Exception as err:
                print(f'Example [{id}] failed | Error: {err}')
                err_dict = {'caption': caption, 'name': wav_name}

                err_meta.append(err_dict)


    # dump err files
    with open(err_path, 'w') as json_file:
        for item in err_meta:
            json.dump(item, json_file)
            json_file.write('\n')  # Add a newline to separate JSON objects

        





