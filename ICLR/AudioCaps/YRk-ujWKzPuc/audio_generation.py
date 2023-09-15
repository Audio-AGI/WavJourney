
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YRk-ujWKzPuc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Heavy rain droplets hitting the ground", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Heavy_rain_droplets_hitting_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Heavy_rain_droplets_hitting_the.wav")))

TTA(text="Continuation of heavy rain hitting the ground", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_heavy_rain_hitting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_heavy_rain_hitting.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Heavy_rain_droplets_hitting_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_heavy_rain_hitting.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YRk-ujWKzPuc.wav"))
