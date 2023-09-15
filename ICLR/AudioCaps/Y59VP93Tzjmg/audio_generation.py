
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y59VP93Tzjmg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Train blowing horn", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Train_blowing_horn.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Train_blowing_horn.wav")))

TTA(text="Approaching train with track sounds", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Approaching_train_with_track_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Approaching_train_with_track_sounds.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Train_blowing_horn.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Approaching_train_with_track_sounds.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y59VP93Tzjmg.wav"))
