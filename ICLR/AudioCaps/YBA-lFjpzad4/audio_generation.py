
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBA-lFjpzad4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="The sound of a vehicle approaching", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_a_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_a_vehicle.wav")))

TTA(text="The sound of a vehicle downshifting", length=3, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_1_The_sound_of_a_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_The_sound_of_a_vehicle.wav")))

TTA(text="The sound of a vehicle passing by", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_a_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_a_vehicle.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_a_vehicle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_The_sound_of_a_vehicle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_a_vehicle.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="General city ambience, faint traffic sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_General_city_ambience_faint_traffic.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_General_city_ambience_faint_traffic.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBA-lFjpzad4.wav"))
