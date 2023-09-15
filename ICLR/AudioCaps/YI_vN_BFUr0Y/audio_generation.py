
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YI_vN_BFUr0Y/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Train horn blowing several times", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_several_times.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_several_times.wav")))

TTA(text="Train horn blowing continuing", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Train_horn_blowing_continuing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Train_horn_blowing_continuing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Train_horn_blowing_several_times.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Train_horn_blowing_continuing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Ring of railroad warning signals", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Ring_of_railroad_warning_signals.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Ring_of_railroad_warning_signals.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YI_vN_BFUr0Y.wav"))
