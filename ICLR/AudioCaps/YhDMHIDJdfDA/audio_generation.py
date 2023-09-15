
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YhDMHIDJdfDA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Deep inhale sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Deep_inhale_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Deep_inhale_sound.wav")))

TTA(text="Brief pause sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Brief_pause_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Brief_pause_sound.wav")))

TTA(text="Loud snoring sound", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Loud_snoring_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Loud_snoring_sound.wav")))

TTA(text="Brief pause sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Brief_pause_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Brief_pause_sound.wav")))

TTA(text="Deep exhale sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Deep_exhale_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Deep_exhale_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Deep_inhale_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Brief_pause_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Loud_snoring_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Brief_pause_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Deep_exhale_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YhDMHIDJdfDA.wav"))
