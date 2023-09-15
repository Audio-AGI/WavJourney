
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YnD1K1Zo0qrM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud clicking noises", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_clicking_noises.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_clicking_noises.wav")))

TTA(text="Sequence of rapid fire gunshots", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sequence_of_rapid_fire_gunshots.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sequence_of_rapid_fire_gunshots.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_clicking_noises.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sequence_of_rapid_fire_gunshots.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Gusting wind", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Gusting_wind.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Gusting_wind.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YnD1K1Zo0qrM.wav"))
