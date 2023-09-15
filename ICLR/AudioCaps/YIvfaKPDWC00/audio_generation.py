
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIvfaKPDWC00/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Hum of accelerating vehicle starting up", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Hum_of_accelerating_vehicle_starting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Hum_of_accelerating_vehicle_starting.wav")))

TTA(text="Sound of accelerating vehicle moving away swiftly", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_accelerating_vehicle_moving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_accelerating_vehicle_moving.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Hum_of_accelerating_vehicle_starting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_accelerating_vehicle_moving.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Emergency sirens wailing in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Emergency_sirens_wailing_in_the.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Emergency_sirens_wailing_in_the.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIvfaKPDWC00.wav"))
