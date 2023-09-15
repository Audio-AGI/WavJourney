
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMtK8L8gXRrI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Water running sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Water_running_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Water_running_sound.wav")))

TTA(text="Toilet flushing sound", length=5, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Toilet_flushing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Toilet_flushing_sound.wav")))

TTA(text="Drip of water sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Drip_of_water_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Drip_of_water_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Water_running_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Toilet_flushing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Drip_of_water_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMtK8L8gXRrI.wav"))
