
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YU3CAjsm1sec/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Several cats meowing in unison", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Several_cats_meowing_in_unison.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Several_cats_meowing_in_unison.wav")))

TTM(text="Man singing a soft tune", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_music_0_Man_singing_a_soft_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Man_singing_a_soft_tune.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Several_cats_meowing_in_unison.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Man_singing_a_soft_tune.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YU3CAjsm1sec.wav"))
