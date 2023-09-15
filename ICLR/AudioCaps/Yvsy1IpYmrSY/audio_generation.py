
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yvsy1IpYmrSY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Muffled car engine revving", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Muffled_car_engine_revving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Muffled_car_engine_revving.wav")))

TTA(text="Tires skidding on pavement", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Tires_skidding_on_pavement.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Tires_skidding_on_pavement.wav")))

TTA(text="Vehicle engine accelerating harshly", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Vehicle_engine_accelerating_harshly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Vehicle_engine_accelerating_harshly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Muffled_car_engine_revving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Tires_skidding_on_pavement.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Vehicle_engine_accelerating_harshly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yvsy1IpYmrSY.wav"))
