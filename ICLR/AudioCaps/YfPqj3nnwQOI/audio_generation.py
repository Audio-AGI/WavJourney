
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YfPqj3nnwQOI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of waves crashing onto the shore", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_waves_crashing_onto.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_waves_crashing_onto.wav")))

TTA(text="The soft rustle of retreating waves", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_The_soft_rustle_of_retreating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_The_soft_rustle_of_retreating.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_waves_crashing_onto.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_The_soft_rustle_of_retreating.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YfPqj3nnwQOI.wav"))
