
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YjYPU6aSDo88/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud humming noise", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_humming_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_humming_noise.wav")))

TTA(text="Continued loud humming", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Continued_loud_humming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Continued_loud_humming.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_humming_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Continued_loud_humming.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Wind blowing softly", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing_softly.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing_softly.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YjYPU6aSDo88.wav"))
