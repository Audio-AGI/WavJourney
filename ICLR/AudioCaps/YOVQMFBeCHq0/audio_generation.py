
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YOVQMFBeCHq0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sirens blaring from a vehicle up close", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sirens_blaring_from_a_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sirens_blaring_from_a_vehicle.wav")))

TTA(text="Sirens blaring from a vehicle moving", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sirens_blaring_from_a_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sirens_blaring_from_a_vehicle.wav")))

TTA(text="The sound of sirens diminishing into the distance", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_sirens_diminishing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_sirens_diminishing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sirens_blaring_from_a_vehicle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sirens_blaring_from_a_vehicle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_sirens_diminishing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YOVQMFBeCHq0.wav"))
