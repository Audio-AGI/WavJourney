
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YhVUmQfBIYe8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Seems like a quiet night. What's on the schedule for today?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Seems_like_a_quiet_night.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Seems_like_a_quiet_night.wav")))

TTA(text="Metal car door clicking open", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Metal_car_door_clicking_open.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Metal_car_door_clicking_open.wav")))

TTA(text="Metal clinks", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_clinks.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_clinks.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Seems_like_a_quiet_night.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Metal_car_door_clicking_open.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_clinks.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Crunching footfalls", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crunching_footfalls.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Slight rustling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Slight_rustling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crunching_footfalls.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Slight_rustling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YhVUmQfBIYe8.wav"))
