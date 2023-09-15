
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIFRmbxWK8u0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_6_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_6_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_7_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_7_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_8_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_8_Clock_ticking_sound.wav")))

TTA(text="Clock ticking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_9_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_9_Clock_ticking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_6_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_7_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_8_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_9_Clock_ticking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIFRmbxWK8u0.wav"))
