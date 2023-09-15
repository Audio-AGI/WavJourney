
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_BSmz3SEW1w/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Pigeons rustling feathers", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Pigeons_rustling_feathers.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Pigeons_rustling_feathers.wav")))

TTA(text="Pigeons cooing sound", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Pigeons_cooing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Pigeons_cooing_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Pigeons_rustling_feathers.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Pigeons_cooing_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_BSmz3SEW1w.wav"))
