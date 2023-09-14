import os
import yaml
import logging
import nltk
import torch
import numpy as np
import torchaudio
from torchaudio.transforms import SpeedPerturbation
from APIs import WRITE_AUDIO, LOUDNESS_NORM
from utils import fade, get_service_port
from flask import Flask, request, jsonify

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Configure the logging format and level
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create a FileHandler for the log file
os.makedirs('services_logs', exist_ok=True)
log_filename = 'services_logs/Wav-API.log'
file_handler = logging.FileHandler(log_filename, mode='w')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add the FileHandler to the root logger
logging.getLogger('').addHandler(file_handler)


"""
Initialize the AudioCraft models here
"""
from audiocraft.models import AudioGen, MusicGen
tta_model_size = config['AudioCraft']['tta_model_size']
tta_model = AudioGen.get_pretrained(f'facebook/audiogen-{tta_model_size}')
logging.info(f'AudioGen ({tta_model_size}) is loaded ...')

ttm_model_size = config['AudioCraft']['ttm_model_size']
ttm_model = MusicGen.get_pretrained(f'facebook/musicgen-{ttm_model_size}')
logging.info(f'MusicGen ({ttm_model_size}) is loaded ...')


"""
Initialize the BarkModel here
"""
# from transformers import BarkModel, AutoProcessor
# tts_model = BarkModel.from_pretrained("suno/bark")
# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# tts_model = tts_model.to(device)
# tts_model = tts_model.to_bettertransformer()    # Flash attention
# SAMPLE_RATE = tts_model.generation_config.sample_rate
# SEMANTIC_TEMPERATURE = 0.9
# COARSE_TEMPERATURE = 0.5
# FINE_TEMPERATURE = 0.5
# processor = AutoProcessor.from_pretrained("suno/bark")

SPEED = float(config['Text-to-Speech']['speed'])
speed_perturb = SpeedPerturbation(32000, [SPEED])

from bark.generation import generate_text_semantic, preload_models
from bark.api import semantic_to_waveform
from bark import SAMPLE_RATE
preload_models()

logging.info('Bark model is loaded ...')


""" 
Initialize the VoiceFixer model here
"""
from voicefixer import VoiceFixer
vf = VoiceFixer()
logging.info('VoiceFixer is loaded ...')


"""
Initalize the VoiceParser model here
"""
from VoiceParser.model import VoiceParser
vp_device = config['Voice-Parser']['device']
vp = VoiceParser(device=vp_device)
logging.info('VoiceParser is loaded ...')


app = Flask(__name__)


@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    # Receive the text from the POST request
    data = request.json
    text = data['text']
    length = float(data.get('length', 5.0))
    volume = float(data.get('volume', -35))
    output_wav = data.get('output_wav', 'out.wav')

    logging.info(f'TTA (AudioGen): Prompt: {text}, length: {length} seconds, volume: {volume} dB')
    
    try:
        tta_model.set_generation_params(duration=length)  
        wav = tta_model.generate([text])  
        wav = torchaudio.functional.resample(wav, orig_freq=16000, new_freq=32000)

        wav = wav.squeeze().cpu().detach().numpy()
        wav = fade(LOUDNESS_NORM(wav, volumn=volume))
        WRITE_AUDIO(wav, name=output_wav)

        # Return success message and the filename of the generated audio
        return jsonify({'message': f'Text-to-Audio generated successfully | {text}', 'file': output_wav})

    except Exception as e:
        return jsonify({'API error': str(e)}), 500


@app.route('/generate_music', methods=['POST'])
def generate_music():
    # Receive the text from the POST request
    data = request.json
    text = data['text']
    length = float(data.get('length', 5.0))
    volume = float(data.get('volume', -35))
    output_wav = data.get('output_wav', 'out.wav')

    logging.info(f'TTM (MusicGen): Prompt: {text}, length: {length} seconds, volume: {volume} dB')


    try:
        ttm_model.set_generation_params(duration=length)  
        wav = ttm_model.generate([text])  
        wav = wav[0][0].cpu().detach().numpy()
        wav = fade(LOUDNESS_NORM(wav, volumn=volume))
        WRITE_AUDIO(wav, name=output_wav)

        # Return success message and the filename of the generated audio
        return jsonify({'message': f'Text-to-Music generated successfully | {text}', 'file': output_wav})

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({'API error': str(e)}), 500


# @app.route('/generate_speech', methods=['POST'])
# def generate_speech():
#     # Receive the text from the POST request
#     data = request.json
#     text = data['text']
#     speaker_id = data['speaker_id']
#     speaker_npz = data['speaker_npz']
#     volume = float(data.get('volume', -35))
#     output_wav = data.get('output_wav', 'out.wav')
    
#     logging.info(f'TTS (Bark): Speaker: {speaker_id}, Volume: {volume} dB, Prompt: {text}')

#     try:   
#         # Generate audio using the global pipe object
#         text = text.replace('\n', ' ').strip()
#         sentences = nltk.sent_tokenize(text)
#         silence = torch.zeros(int(0.1 * SAMPLE_RATE), device=device).unsqueeze(0)  # 0.1 second of silence

#         pieces = []
#         for sentence in sentences:
#             inputs = processor(sentence, voice_preset=speaker_npz).to(device)
#             # NOTE: you must run the line below, otherwise you will see the runtime error
#             # RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.
#             inputs['history_prompt']['coarse_prompt'] = inputs['history_prompt']['coarse_prompt'].transpose(0, 1).contiguous().transpose(0, 1)

#             with torch.inference_mode():
#                 # TODO: min_eos_p?
#                 output = tts_model.generate(
#                     **inputs,
#                     do_sample = True,
#                     semantic_temperature = SEMANTIC_TEMPERATURE,
#                     coarse_temperature = COARSE_TEMPERATURE,
#                     fine_temperature = FINE_TEMPERATURE
#                 )

#             pieces += [output, silence]

#         result_audio = torch.cat(pieces, dim=1)
#         wav_tensor = result_audio.to(dtype=torch.float32).cpu()
#         wav = torchaudio.functional.resample(wav_tensor, orig_freq=SAMPLE_RATE, new_freq=32000)
#         wav = speed_perturb(wav.float())[0].squeeze(0)
#         wav = wav.numpy()
#         wav = LOUDNESS_NORM(wav, volumn=volume)
#         WRITE_AUDIO(wav, name=output_wav)

#         # Return success message and the filename of the generated audio
#         return jsonify({'message': f'Text-to-Speech generated successfully | {speaker_id}: {text}', 'file': output_wav})

#     except Exception as e:
#         # Return error message if something goes wrong
#         return jsonify({'API error': str(e)}), 500


@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    # Receive the text from the POST request
    data = request.json
    text = data['text']
    speaker_id = data['speaker_id']
    speaker_npz = data['speaker_npz']
    volume = float(data.get('volume', -35))
    output_wav = data.get('output_wav', 'out.wav')
    
    logging.info(f'TTS (Bark): Speaker: {speaker_id}, Volume: {volume} dB, Prompt: {text}')

    try:   
        # Generate audio using the global pipe object
        script = text.replace("\n", " ").strip()
        sentences = nltk.sent_tokenize(script)

        GEN_TEMP = 0.9
        silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

        pieces = []
        for sentence in sentences:
            semantic_tokens = generate_text_semantic(
                sentence,
                history_prompt=speaker_npz,
                temp=GEN_TEMP,
                min_eos_p=0.05,  # this controls how likely the generation is to end
            )

            audio_array = semantic_to_waveform(semantic_tokens, history_prompt=speaker_npz, temp=0.5)
            pieces += [audio_array, silence.copy()]

        result_audio = np.concatenate(pieces)
        wav_tensor = torch.tensor(result_audio).unsqueeze(0)
        wav = torchaudio.functional.resample(wav_tensor, orig_freq=SAMPLE_RATE, new_freq=32000)
        wav = speed_perturb(wav.float())[0].squeeze(0)
        wav = wav.numpy()
        wav = LOUDNESS_NORM(wav, volumn=volume)
        WRITE_AUDIO(wav, name=output_wav)

        # Return success message and the filename of the generated audio
        return jsonify({'message': f'Text-to-Speech generated successfully | {speaker_id}: {text}', 'file': output_wav})

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({'API error': str(e)}), 500


@app.route('/fix_audio', methods=['POST'])
def fix_audio():
    # Receive the text from the POST request
    data = request.json
    processfile = data['processfile']

    logging.info(f'Fixing {processfile} ...')

    try:
        vf.restore(input=processfile, output=processfile, cuda=True, mode=0)
        
        # Return success message and the filename of the generated audio
        return jsonify({'message': 'Speech restored successfully', 'file': processfile})

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({'API error': str(e)}), 500


@app.route('/parse_voice', methods=['POST'])
def parse_voice():
    # Receive the text from the POST request
    data = request.json
    wav_path = data['wav_path']
    out_dir = data['out_dir']

    logging.info(f'Parsing {wav_path} ...')

    try:
        vp.extract_acoustic_embed(wav_path, out_dir)
        
        # Return success message and the filename of the generated audio
        return jsonify({'message': f'Sucessfully parsed {wav_path}'})

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({'API error': str(e)}), 500


if __name__ == '__main__':
    service_port = get_service_port()
    # We disable multithreading to force services to process one request at a time and avoid CUDA OOM
    app.run(debug=False, threaded=False, port=service_port)
