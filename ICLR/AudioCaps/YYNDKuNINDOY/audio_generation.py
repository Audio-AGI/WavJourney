
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YYNDKuNINDOY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Emergency siren wailing in the distance", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Emergency_siren_wailing_in_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Emergency_siren_wailing_in_the.wav")))

TTA(text="Loud truck horn honking", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_truck_horn_honking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_truck_horn_honking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Emergency_siren_wailing_in_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_truck_horn_honking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="The low rumble of a large truck engine", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_The_low_rumble_of_a.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_The_low_rumble_of_a.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YYNDKuNINDOY.wav"))
