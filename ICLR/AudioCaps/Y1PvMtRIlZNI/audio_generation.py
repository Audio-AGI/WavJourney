
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1PvMtRIlZNI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Stream of water trickling", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Stream_of_water_trickling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Stream_of_water_trickling.wav")))

TTA(text="Plastic clanks against a metal surface", length=2, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_clanks_against_a_metal.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_clanks_against_a_metal.wav")))

TTA(text="Water pouring down a drain", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Water_pouring_down_a_drain.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Water_pouring_down_a_drain.wav")))

TTA(text="Camera muffling effect", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Camera_muffling_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Camera_muffling_effect.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Stream_of_water_trickling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_clanks_against_a_metal.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Water_pouring_down_a_drain.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Camera_muffling_effect.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:4])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Gentle breeze and rustling leaves", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Gentle_breeze_and_rustling_leaves.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Distant birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Distant_birds_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Gentle_breeze_and_rustling_leaves.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Distant_birds_chirping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1PvMtRIlZNI.wav"))
