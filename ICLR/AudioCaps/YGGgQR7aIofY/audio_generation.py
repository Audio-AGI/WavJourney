
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YGGgQR7aIofY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a loud horn", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_loud_horn.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_loud_horn.wav")))

TTA(text="Sound of wind blowing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_wind_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_wind_blowing.wav")))

TTA(text="Sound of a motor vehicle engine running", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_motor_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_motor_vehicle.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_loud_horn.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_wind_blowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_motor_vehicle.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YGGgQR7aIofY.wav"))
