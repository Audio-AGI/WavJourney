import os
import json, json5
from pathlib import Path

import utils
from APIs import VP


def save_voice_presets_metadata(voice_presets_path, metadata):
    with open(voice_presets_path / 'metadata.json', 'w') as f:
        json.dump(metadata, f, indent=4)

def load_voice_presets_metadata(voice_presets_path, safe_if_metadata_not_exist=False):
    metadata_full_path = Path(voice_presets_path) / 'metadata.json'

    if safe_if_metadata_not_exist:
        if not os.path.exists(metadata_full_path):
            return {}

    with open(metadata_full_path, 'r') as f:
        presets = json5.load(f)

    return presets

# return system voice presets and session voice presets individually, each in a list
def get_voice_presets(session_id):
    system_presets, session_presets = [], []

    # Load system presets
    system_presets = load_voice_presets_metadata(utils.get_system_voice_preset_path())

    # Load session presets
    session_presets = load_voice_presets_metadata(
        utils.get_session_voice_preset_path(session_id),
        safe_if_metadata_not_exist=True
    )

    return system_presets, session_presets

# return merged voice presets in a {voice_preset_name: voice_preset} dict
def get_merged_voice_presets(session_id):
    system_presets, session_presets = get_voice_presets(session_id)
    res = {}
    for preset in list(system_presets.values()) + list(session_presets.values()):
        res[preset['id']] = preset  # session presets with the same id will cover that of system presets
    return res

def add_voice_preset(voice_presets_path, presets, id, desc, wav_file_path):
    if id in presets:
        raise KeyError(f'{id} already in voice preset, path={voice_presets_path}!')

    # Convert wav to npz
    npz_path = voice_presets_path / 'npz'
    VP(wav_file_path, npz_path)
    npz_file_path = npz_path / f'{Path(wav_file_path).stem}.npz'

    presets[id]  = {
        'id': id,
        'desc': desc,
        'npz_path': str(npz_file_path)
    }
    save_voice_presets_metadata(voice_presets_path, presets)
    return presets[id]

def add_session_voice_preset(id, desc, wav_file_path, session_id):
    voice_presets_path = utils.get_session_voice_preset_path(session_id)
    os.makedirs(voice_presets_path / 'npz', exist_ok=True)
    presets = load_voice_presets_metadata(voice_presets_path, safe_if_metadata_not_exist=True)
    if len(presets) >= 3:
        raise ValueError(f'session voice presets size exceed 3')
    if id in presets:
        raise KeyError(f'{id} already in voice preset, path={voice_presets_path}!')

    return add_voice_preset(voice_presets_path, presets, id, desc, wav_file_path)

def add_system_voice_preset(id, desc, wav_file_path):
    voice_presets_path = utils.get_system_voice_preset_path()
    presets = load_voice_presets_metadata(voice_presets_path)
    return add_voice_preset(voice_presets_path, presets, id, desc, wav_file_path)

# if session_id set to '', we are removing system voice presets
def remove_session_voice_preset(id, session_id):
    voice_presets_path = utils.get_session_voice_preset_path(session_id)
    presets = load_voice_presets_metadata(
        voice_presets_path,
        safe_if_metadata_not_exist=True
    )
    preset = presets.pop(id)
    npz_path = preset['npz_path']

    try:
        os.remove(npz_path)
    except FileNotFoundError:
        print(f"INFO: trying to delete {npz_path} which does not exist, path={voice_presets_path}.")

    save_voice_presets_metadata(voice_presets_path, presets)