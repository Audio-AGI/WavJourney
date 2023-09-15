
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ya3GzZKxUTy8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Birds chirping", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Birds_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Birds_chirping.wav")))

TTA(text="Duck quacking", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Duck_quacking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Duck_quacking.wav")))

TTA(text="Dog barking", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Dog_barking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Dog_barking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Birds_chirping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Duck_quacking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Dog_barking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ya3GzZKxUTy8.wav"))
