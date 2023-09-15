
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y5ORpSk5CIWc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vibrations from a small engine gradually increasing in volume", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vibrations_from_a_small_engine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vibrations_from_a_small_engine.wav")))

TTA(text="The small engine sound at its loudest as it passes by", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_The_small_engine_sound_at.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_The_small_engine_sound_at.wav")))

TTA(text="The small engine sound fading away into the distance", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_The_small_engine_sound_fading.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_The_small_engine_sound_fading.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vibrations_from_a_small_engine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_The_small_engine_sound_at.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_The_small_engine_sound_fading.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y5ORpSk5CIWc.wav"))
