
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ycr0GiZr0TNY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Giggling and laughing of babies", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Giggling_and_laughing_of_babies.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Giggling_and_laughing_of_babies.wav")))

TTA(text="Fizzing sound effect, like a soda can opening", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Fizzing_sound_effect_like_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Fizzing_sound_effect_like_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Giggling_and_laughing_of_babies.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Fizzing_sound_effect_like_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ycr0GiZr0TNY.wav"))
