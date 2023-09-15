
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yo7-X8DAToGc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle accelerating", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_accelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_accelerating.wav")))

TTA(text="Sound of a vehicle driving by", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_vehicle_driving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_vehicle_driving.wav")))

TTA(text="Vehicle accelerating", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Vehicle_accelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Vehicle_accelerating.wav")))

TTA(text="Sound of a vehicle driving by", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sound_of_a_vehicle_driving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_a_vehicle_driving.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_accelerating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_vehicle_driving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Vehicle_accelerating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_a_vehicle_driving.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yo7-X8DAToGc.wav"))
