
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHeEa1GZpUGI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Several gunshots sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Several_gunshots_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Several_gunshots_sound.wav")))

TTA(text="Gun_empty click sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Gun_empty_click_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Gun_empty_click_sound.wav")))

TTA(text="Glass breaking sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Glass_breaking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Glass_breaking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Several_gunshots_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Gun_empty_click_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Glass_breaking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHeEa1GZpUGI.wav"))
