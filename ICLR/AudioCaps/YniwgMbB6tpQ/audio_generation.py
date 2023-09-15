
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YniwgMbB6tpQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="High-pitched snoring sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Highpitched_snoring_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Highpitched_snoring_sound.wav")))

TTA(text="Period of silence", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Period_of_silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Period_of_silence.wav")))

TTA(text="High-pitched snoring sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Highpitched_snoring_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Highpitched_snoring_sound.wav")))

TTA(text="Period of silence", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Period_of_silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Period_of_silence.wav")))

TTA(text="High-pitched snoring sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Highpitched_snoring_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Highpitched_snoring_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Highpitched_snoring_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Period_of_silence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Highpitched_snoring_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Period_of_silence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Highpitched_snoring_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YniwgMbB6tpQ.wav"))
