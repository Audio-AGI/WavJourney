
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y3ndid3jni7M/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Train horn blowing several times", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_several_times.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_several_times.wav")))

TTA(text="Railroad crossing signal ringing", length=7, volume=-16, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Railroad_crossing_signal_ringing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Railroad_crossing_signal_ringing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_several_times.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Railroad_crossing_signal_ringing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Train running on railroad tracks", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Train_running_on_railroad_tracks.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Train_running_on_railroad_tracks.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y3ndid3jni7M.wav"))
