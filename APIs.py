import os
import numpy as np
import requests
import yaml
import pyloudnorm as pyln
from scipy.io.wavfile import write
import torchaudio
from retrying import retry
from utils import get_service_port, get_service_url
 

os.environ['OPENBLAS_NUM_THREADS'] = '1'
SAMPLE_RATE = 32000


with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    service_port = get_service_port()
    localhost_addr = get_service_url()
    enable_sr = config['Speech-Restoration']['Enable']

def LOUDNESS_NORM(audio, sr=32000, volumn=-25):
    # peak normalize audio to -1 dB
    peak_normalized_audio = pyln.normalize.peak(audio, -10.0)
    # measure the loudness first 
    meter = pyln.Meter(sr) # create BS.1770 meter
    loudness = meter.integrated_loudness(peak_normalized_audio)
    # loudness normalize audio to -12 dB LUFS
    normalized_audio = pyln.normalize.loudness(peak_normalized_audio, loudness, volumn)
    return normalized_audio
    

def WRITE_AUDIO(wav, name=None, sr=SAMPLE_RATE):
    """
    function: write audio numpy to .wav file
    @params:
        wav: np.array [samples]
    """   
    if name is None:
        name = 'output.wav' 
    
    if len(wav.shape) > 1:
        wav = wav[0]

    # declipping
    
    max_value = np.max(np.abs(wav))
    if max_value > 1:
        wav *= 0.9 / max_value
    
    # write audio
    write(name, sr, np.round(wav*32767).astype(np.int16))


def READ_AUDIO_NUMPY(wav, sr=SAMPLE_RATE):
    """
    function: read audio numpy 
    return: np.array [samples]
    """
    waveform, sample_rate = torchaudio.load(wav)

    if sample_rate != sr:
        waveform = torchaudio.functional.resample(waveform, orig_freq=sample_rate, new_freq=sr)
    
    wav_numpy = waveform[0].numpy()

    return wav_numpy


def MIX(wavs=[['1.wav', 0.], ['2.wav', 10.]], out_wav='out.wav', sr=SAMPLE_RATE):
    """
    wavs:[[wav_name, absolute_offset], ...]
    """

    max_length = max([int(wav[1]*sr + len(READ_AUDIO_NUMPY(wav[0]))) for wav in wavs])
    template_wav = np.zeros(max_length)

    for wav in wavs:
        cur_name, cur_offset = wav
        cur_wav = READ_AUDIO_NUMPY(cur_name)
        cur_len = len(cur_wav)
        cur_offset = int(cur_offset * sr)
        
        # mix
        template_wav[cur_offset:cur_offset+cur_len] += cur_wav
    
    WRITE_AUDIO(template_wav, name=out_wav)


def CAT(wavs, out_wav='out.wav'):
    """
    wavs: List of wav file ['1.wav', '2.wav', ...]
    """
    wav_num = len(wavs)

    segment0 = READ_AUDIO_NUMPY(wavs[0])

    cat_wav = segment0

    if wav_num > 1:
        for i in range(1, wav_num):
            next_wav = READ_AUDIO_NUMPY(wavs[i])
            cat_wav = np.concatenate((cat_wav, next_wav), axis=-1)

    WRITE_AUDIO(cat_wav, name=out_wav)


def COMPUTE_LEN(wav):
    wav= READ_AUDIO_NUMPY(wav)
    return len(wav) / 32000


@retry(stop_max_attempt_number=5, wait_fixed=2000)
def TTM(text, length=10, volume=-28, out_wav='out.wav'):
    url = f'http://{localhost_addr}:{service_port}/generate_music'
    data = {
        'text': f'{text}',
        'length': f'{length}',
        'volume': f'{volume}',
        'output_wav': f'{out_wav}',
    }
    
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print('Success:', response.json()['message'])
    else:
        print('Error:', response.json()['API error'])
        raise RuntimeError(response.json()['API error'])

@retry(stop_max_attempt_number=5, wait_fixed=2000)
def TTA(text, length=5, volume=-35, out_wav='out.wav'):
    url = f'http://{localhost_addr}:{service_port}/generate_audio'
    data = {
        'text': f'{text}',
        'length': f'{length}',
        'volume': f'{volume}',
        'output_wav': f'{out_wav}',
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print('Success:', response.json()['message'])
    else:
        print('Error:', response.json()['API error'])
        raise RuntimeError(response.json()['API error'])


@retry(stop_max_attempt_number=5, wait_fixed=2000)
def TTS(text, volume=-20, out_wav='out.wav', enhanced=enable_sr, speaker_id='', speaker_npz=''):
    url = f'http://{localhost_addr}:{service_port}/generate_speech'
    data = {
    'text': f'{text}',
    'speaker_id': f'{speaker_id}',
    'speaker_npz': f'{speaker_npz}',
    'volume': f'{volume}',
    'output_wav': f'{out_wav}',
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print('Success:', response.json()['message'])
    else:
        print('Error:', response.json()['API error'])
        raise RuntimeError(response.json()['API error'])

    if enhanced:
        SR(processfile=out_wav)


@retry(stop_max_attempt_number=5, wait_fixed=2000)
def SR(processfile):
    url = f'http://{localhost_addr}:{service_port}/fix_audio'
    data = {'processfile': f'{processfile}'}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print('Success:', response.json()['message'])
    else:
        print('Error:', response.json()['API error'])
        raise RuntimeError(response.json()['API error'])


@retry(stop_max_attempt_number=5, wait_fixed=2000)
def VP(wav_path, out_dir):
    url = f'http://{localhost_addr}:{service_port}/parse_voice'
    data = {
        'wav_path': f'{wav_path}', 
        'out_dir':f'{out_dir}'
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print('Success:', response.json()['message'])
    else:
        print('Error:', response.json()['API error'])
        raise RuntimeError(response.json()['API error'])

