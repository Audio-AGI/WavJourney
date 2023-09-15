
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YkHIe4CfaccQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Goat bleats first time", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Goat_bleats_first_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Goat_bleats_first_time.wav")))

TTA(text="Goat bleats second time", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Goat_bleats_second_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Goat_bleats_second_time.wav")))

TTA(text="Goat bleats third time", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Goat_bleats_third_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Goat_bleats_third_time.wav")))

TTA(text="Goat bleats fourth time", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Goat_bleats_fourth_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Goat_bleats_fourth_time.wav")))

TTA(text="Goat bleats fifth time", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Goat_bleats_fifth_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Goat_bleats_fifth_time.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Goat_bleats_first_time.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Goat_bleats_second_time.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Goat_bleats_third_time.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Goat_bleats_fourth_time.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Goat_bleats_fifth_time.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YkHIe4CfaccQ.wav"))
