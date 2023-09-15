
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YOMGHnJV0l2U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Metal scrapping against a wooden surface", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Metal_scrapping_against_a_wooden.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Metal_scrapping_against_a_wooden.wav")))

TTA(text="Sand scrapping", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sand_scrapping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sand_scrapping.wav")))

TTA(text="More metal scrapping against a wooden surface", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_More_metal_scrapping_against_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_More_metal_scrapping_against_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Metal_scrapping_against_a_wooden.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sand_scrapping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_More_metal_scrapping_against_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YOMGHnJV0l2U.wav"))
