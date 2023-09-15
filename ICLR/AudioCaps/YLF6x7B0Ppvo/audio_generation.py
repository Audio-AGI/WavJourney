
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YLF6x7B0Ppvo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Mid-size motor vehicle engine running fast", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Midsize_motor_vehicle_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Midsize_motor_vehicle_engine_running.wav")))

TTA(text="Gears changing", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Gears_changing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Gears_changing.wav")))

TTA(text="Motor vehicle accelerating", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Motor_vehicle_accelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Motor_vehicle_accelerating.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Midsize_motor_vehicle_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Gears_changing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Motor_vehicle_accelerating.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YLF6x7B0Ppvo.wav"))
