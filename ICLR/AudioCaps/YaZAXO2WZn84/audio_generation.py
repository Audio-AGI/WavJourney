
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YaZAXO2WZn84/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Bells chiming", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Bells_chiming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Bells_chiming.wav")))

TTA(text="Lawn mower engine running", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Lawn_mower_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Lawn_mower_engine_running.wav")))

TTA(text="Steam engine running and train whistle blowing", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Steam_engine_running_and_train.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Steam_engine_running_and_train.wav")))

TTA(text="Bells chiming", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Bells_chiming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Bells_chiming.wav")))

TTA(text="Lawn mower engine running", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Lawn_mower_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Lawn_mower_engine_running.wav")))

TTA(text="Steam engine running and train whistle blowing", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Steam_engine_running_and_train.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Steam_engine_running_and_train.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Bells_chiming.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Lawn_mower_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Steam_engine_running_and_train.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Bells_chiming.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Lawn_mower_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Steam_engine_running_and_train.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:6])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Crowd of people talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_talking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YaZAXO2WZn84.wav"))
