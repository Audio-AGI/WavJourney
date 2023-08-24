import os
import re
import torch
import  numpy as np
import yaml
from pathlib import Path


#### path related code BEGIN ####
def get_session_path(session_id):
    return Path(f'output/sessions/{session_id}')

def get_system_voice_preset_path():
    return Path('data/voice_presets')
    
def get_session_voice_preset_path(session_id):
    return Path(f'{get_session_path(session_id)}/voice_presets')
    
def get_session_audio_path(session_id):
    return Path(f'{get_session_path(session_id)}/audio')

def rescale_to_match_energy(segment1, segment2):
    ratio = get_energy_ratio(segment1, segment2)
    recaled_segment1 = segment1 / ratio
    return recaled_segment1.numpy()
#### path related code END ####

def text_to_abbrev_prompt(input_text):
    return re.sub(r'[^a-zA-Z_]', '', '_'.join(input_text.split()[:5]))

def get_energy(x):
    return np.mean(x ** 2)


def get_energy_ratio(segment1, segment2):
    energy1 = get_energy(segment1)
    energy2 = max(get_energy(segment2), 1e-10)
    ratio = (energy1 / energy2) ** 0.5
    ratio = torch.tensor(ratio)
    ratio = torch.clamp(ratio, 0.02, 50)
    return ratio

def fade(audio_data, fade_duration=2, sr=32000):
    audio_duration = audio_data.shape[0] / sr

    # automated choose fade duration
    if audio_duration >=8:
         # keep fade_duration 2
        pass
    else:
        fade_duration = audio_duration / 5

    fade_sampels = int(sr * fade_duration)
    fade_in = np.linspace(0, 1, fade_sampels)
    fade_out = np.linspace(1, 0, fade_sampels)

    audio_data_fade_in = audio_data[:fade_sampels] * fade_in
    audio_data_fade_out = audio_data[-fade_sampels:] * fade_out

    audio_data_faded = np.concatenate((audio_data_fade_in, audio_data[len(fade_in):-len(fade_out)], audio_data_fade_out))
    return audio_data_faded

# def get_key(config='config.yaml'):
#     with open('config.yaml', 'r') as file:
#         config = yaml.safe_load(file)
#         return config['OpenAI-Key'] if 'OpenAI-Key' in config else None

def get_service_port():
    service_port = os.environ.get('WAVJOURNEY_SERVICE_PORT')
    return service_port

def get_service_url():
    service_url = os.environ.get('WAVJOURNEY_SERVICE_URL')
    return service_url 

def get_api_key():
    api_key = os.environ.get('WAVJOURNEY_OPENAI_KEY')
    return api_key       

def get_max_script_lines():
    max_lines = int(os.environ.get('WAVJOURNEY_MAX_SCRIPT_LINES', 999))
    return max_lines