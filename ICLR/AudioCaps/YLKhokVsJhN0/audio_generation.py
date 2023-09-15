
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YLKhokVsJhN0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="One sheep baaing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_One_sheep_baaing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_One_sheep_baaing.wav")))

TTA(text="Two more sheep join, baaing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Two_more_sheep_join_baaing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Two_more_sheep_join_baaing.wav")))

TTA(text="Several more sheep joining, baaing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Several_more_sheep_joining_baaing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Several_more_sheep_joining_baaing.wav")))

TTA(text="The rest of the sheep join, baaing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_The_rest_of_the_sheep.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_The_rest_of_the_sheep.wav")))

TTA(text="The herd of sheep continues baaing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_The_herd_of_sheep_continues.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_The_herd_of_sheep_continues.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_One_sheep_baaing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Two_more_sheep_join_baaing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Several_more_sheep_joining_baaing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_The_rest_of_the_sheep.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_The_herd_of_sheep_continues.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YLKhokVsJhN0.wav"))
