
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YOt0bN_hz2ec/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Train horn blowing twice", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_twice.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_twice.wav")))

TTA(text="Sound of train speeding down the tracks", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_train_speeding_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_train_speeding_down.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_twice.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_train_speeding_down.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YOt0bN_hz2ec.wav"))
