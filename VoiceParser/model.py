import os
import json
import numpy as np

import torch
import torchaudio
torchaudio.set_audio_backend("soundfile")  # Use 'soundfile' backend

from encodec import EncodecModel
from encodec.utils import convert_audio
from .hubert_manager import HuBERTManager
from .pre_kmeans_hubert import CustomHubert
from .customtokenizer import CustomTokenizer

class VoiceParser():
    def __init__(self, device='cpu'):
        model = ('quantifier_hubert_base_ls960_14.pth', 'tokenizer.pth')

        hubert_model = CustomHubert(HuBERTManager.make_sure_hubert_installed(), device=device)
        quant_model = CustomTokenizer.load_from_checkpoint(HuBERTManager.make_sure_tokenizer_installed(model=model[0], local_file=model[1]), device)
        encodec_model = EncodecModel.encodec_model_24khz()
        encodec_model.set_target_bandwidth(6.0)
        
        self.hubert_model = hubert_model
        self.quant_model = quant_model
        self.encodec_model = encodec_model.to(device)
        self.device = device
        print('Loaded VoiceParser models!')


    def extract_acoustic_embed(self, wav_path, npz_dir):
        wav, sr = torchaudio.load(wav_path)

        wav_hubert = wav.to(self.device)

        if wav_hubert.shape[0] == 2:  # Stereo to mono if needed
            wav_hubert = wav_hubert.mean(0, keepdim=True)
        
        semantic_vectors = self.hubert_model.forward(wav_hubert, input_sample_hz=sr)
        semantic_tokens = self.quant_model.get_token(semantic_vectors)
        wav = convert_audio(wav, sr, self.encodec_model.sample_rate, 1).unsqueeze(0)

        wav = wav.to(self.device)
        
        with torch.no_grad():
            encoded_frames = self.encodec_model.encode(wav)

        codes = torch.cat([encoded[0] for encoded in encoded_frames], dim=-1).squeeze()
        
        codes = codes.cpu()
        semantic_tokens = semantic_tokens.cpu()

        wav_name = os.path.split(wav_path)[1]
        npz_name = wav_name[:-4] + '.npz'
        npz_path = os.path.join(npz_dir, npz_name)

        np.savez(
         npz_path,
         semantic_prompt=semantic_tokens,
         fine_prompt=codes,
         coarse_prompt=codes[:2, :]
        )

        return npz_path


    def read_json_file(self, json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
        return data


    def parse_voice_json(self, voice_json, output_dir):
        """
        Parse a voice json file, generate the corresponding output json and npz files
        Params:
        voice_json: path of a json file or List of json nodes
        output_dir: output dir for new json and npz files
        """
        if isinstance(voice_json, list):
            voice_json = voice_json
        else:
            # If voice_json is a file path (str), read the JSON file
            voice_json = self.read_json_file(voice_json)
        for item in voice_json:
            wav_path = item['wav']
            npz_path = self.extract_acoustic_embed(wav_path=wav_path, npz_dir=output_dir)
            item['npz'] = npz_path
            del item['wav']

            output_json = os.path.join(output_dir, 'metadata.json')
        
        with open(output_json, 'w') as file:
            json.dump(voice_json, file, indent=4)








