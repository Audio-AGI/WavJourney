
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2UNuMbxz9ds/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle engine revving", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_revving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_revving.wav")))

TTA(text="Acceleration sound of a vehicle", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Acceleration_sound_of_a_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Acceleration_sound_of_a_vehicle.wav")))

TTA(text="Whipping sound of a metal surface", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Whipping_sound_of_a_metal.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Whipping_sound_of_a_metal.wav")))

TTA(text="Tires skidding sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Tires_skidding_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Tires_skidding_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_revving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Acceleration_sound_of_a_vehicle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Whipping_sound_of_a_metal.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Tires_skidding_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2UNuMbxz9ds.wav"))
