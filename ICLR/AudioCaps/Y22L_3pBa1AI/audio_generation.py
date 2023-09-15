
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y22L_3pBa1AI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Race car driving by at high speed", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Race_car_driving_by_at.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Race_car_driving_by_at.wav")))

TTA(text="Different race car driving by at high speed", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Different_race_car_driving_by.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Different_race_car_driving_by.wav")))

TTA(text="Another race car driving by and fading into the distance", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Another_race_car_driving_by.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Another_race_car_driving_by.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Race_car_driving_by_at.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Different_race_car_driving_by.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Another_race_car_driving_by.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Race track ambiance, crowd cheers", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Race_track_ambiance_crowd_cheers.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Race_track_ambiance_crowd_cheers.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y22L_3pBa1AI.wav"))
