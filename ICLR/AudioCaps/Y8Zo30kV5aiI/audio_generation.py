
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y8Zo30kV5aiI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a car engine, black car starts moving", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_car_engine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_car_engine.wav")))

TTA(text="Siren of ambulance approaching", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Siren_of_ambulance_approaching.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Siren_of_ambulance_approaching.wav")))

TTA(text="Ambulance passing by, siren fades", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Ambulance_passing_by_siren_fades.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Ambulance_passing_by_siren_fades.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_car_engine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Siren_of_ambulance_approaching.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Ambulance_passing_by_siren_fades.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="City street ambiance, cars driving", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_City_street_ambiance_cars_driving.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_City_street_ambiance_cars_driving.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y8Zo30kV5aiI.wav"))
