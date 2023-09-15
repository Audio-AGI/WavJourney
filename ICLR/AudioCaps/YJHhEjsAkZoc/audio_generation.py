
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YJHhEjsAkZoc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Train horn blowing and then fading", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_and_then.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_and_then.wav")))

TTA(text="Metal clacking sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_clacking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_clacking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_and_then.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_clacking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YJHhEjsAkZoc.wav"))
