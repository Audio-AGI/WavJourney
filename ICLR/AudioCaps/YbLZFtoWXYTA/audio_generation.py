
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YbLZFtoWXYTA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Liquid trickling sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Liquid_trickling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Liquid_trickling_sound.wav")))

TTA(text="Liquid splashing as being poured into the container", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Liquid_splashing_as_being_poured.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Liquid_splashing_as_being_poured.wav")))

TTA(text="Gurgling sound of liquid filling up the container", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Gurgling_sound_of_liquid_filling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Gurgling_sound_of_liquid_filling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Liquid_trickling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Liquid_splashing_as_being_poured.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Gurgling_sound_of_liquid_filling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YbLZFtoWXYTA.wav"))
