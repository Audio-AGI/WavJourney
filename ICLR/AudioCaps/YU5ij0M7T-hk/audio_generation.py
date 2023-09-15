
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YU5ij0M7T-hk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A soft rustling sound like leaves in the wind", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_soft_rustling_sound_like.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_soft_rustling_sound_like.wav")))

TTS(text="What a peaceful day it is!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_peaceful_day_it.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_peaceful_day_it.wav")))

TTA(text="The low creaking of an old wooden door slowly opening", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_The_low_creaking_of_an.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_The_low_creaking_of_an.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_soft_rustling_sound_like.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_peaceful_day_it.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_The_low_creaking_of_an.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YU5ij0M7T-hk.wav"))
