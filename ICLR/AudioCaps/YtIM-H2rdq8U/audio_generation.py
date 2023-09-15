
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtIM-H2rdq8U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Gunshots being fired", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Gunshots_being_fired.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Gunshots_being_fired.wav")))

TTA(text="Loud exhale of person", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_exhale_of_person.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_exhale_of_person.wav")))

TTA(text="Gunshots being fired", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Gunshots_being_fired.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Gunshots_being_fired.wav")))

TTA(text="Exhale of person", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Exhale_of_person.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Exhale_of_person.wav")))

TTA(text="Footsteps on stone surface", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Footsteps_on_stone_surface.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Footsteps_on_stone_surface.wav")))

TTA(text="Footsteps on stone surface", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Footsteps_on_stone_surface.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Footsteps_on_stone_surface.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Gunshots_being_fired.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_exhale_of_person.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Gunshots_being_fired.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Exhale_of_person.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Footsteps_on_stone_surface.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Footsteps_on_stone_surface.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:5])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Revolver chamber spinning sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Revolver_chamber_spinning_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[5:6])
bg_audio_offset = sum(fg_audio_lens[:5])
TTA(text="Beating heart sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Beating_heart_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Revolver_chamber_spinning_sound.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Beating_heart_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtIM-H2rdq8U.wav"))
