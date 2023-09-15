
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YDzKjogSVOLM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A duck quacks", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_duck_quacks.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_duck_quacks.wav")))

TTA(text="A rooster crows", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_rooster_crows.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_rooster_crows.wav")))

TTA(text="A girl laughing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_A_girl_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_A_girl_laughing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_duck_quacks.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_rooster_crows.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_A_girl_laughing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="The sound of a crowd chattering", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_The_sound_of_a_crowd.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_The_sound_of_a_crowd.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YDzKjogSVOLM.wav"))
