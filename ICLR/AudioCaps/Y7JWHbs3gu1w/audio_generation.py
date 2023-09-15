
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7JWHbs3gu1w/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a train running on railroad tracks", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_train_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_train_running.wav")))

TTA(text="Train horn honking", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Train_horn_honking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Train_horn_honking.wav")))

TTA(text="Railroad signal bells chiming", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Railroad_signal_bells_chiming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Railroad_signal_bells_chiming.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_train_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Train_horn_honking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Railroad_signal_bells_chiming.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7JWHbs3gu1w.wav"))
