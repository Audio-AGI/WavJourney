
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YKVAIaRPry24/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Plastic clacking sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_sound.wav")))

TTA(text="Plastic slapping a hard surface", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_slapping_a_hard_surface.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_slapping_a_hard_surface.wav")))

TTA(text="Recurring plastic clacking sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Recurring_plastic_clacking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Recurring_plastic_clacking_sound.wav")))

TTA(text="Recurring plastic slapping a hard surface", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Recurring_plastic_slapping_a_hard.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Recurring_plastic_slapping_a_hard.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_slapping_a_hard_surface.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Recurring_plastic_clacking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Recurring_plastic_slapping_a_hard.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Insect buzzing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Insect_buzzing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Insect_buzzing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YKVAIaRPry24.wav"))
