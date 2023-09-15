
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YAUmY0YRAFQE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Siren sound blaring from a close distance", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Siren_sound_blaring_from_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Siren_sound_blaring_from_a.wav")))

TTA(text="Eco of siren sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Eco_of_siren_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Eco_of_siren_sound.wav")))

TTA(text="Siren sound fading into the distance", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Siren_sound_fading_into_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Siren_sound_fading_into_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Siren_sound_blaring_from_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Eco_of_siren_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Siren_sound_fading_into_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Sound of a vehicle passing by", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_vehicle_passing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_vehicle_passing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YAUmY0YRAFQE.wav"))
