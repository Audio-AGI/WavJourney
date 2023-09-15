
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ysl_Pxpc7beo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of vehicle moving over pavement", length=8, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_vehicle_moving_over.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_vehicle_moving_over.wav")))

TTA(text="Loud horn honking noise", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_horn_honking_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_horn_honking_noise.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_vehicle_moving_over.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_horn_honking_noise.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ysl_Pxpc7beo.wav"))
