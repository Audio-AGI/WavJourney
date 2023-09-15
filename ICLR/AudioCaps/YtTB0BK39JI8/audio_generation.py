
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtTB0BK39JI8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Bells ringing", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Bells_ringing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Bells_ringing.wav")))

TTA(text="Wood shuffling and clacking", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Wood_shuffling_and_clacking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Wood_shuffling_and_clacking.wav")))

TTA(text="Bells ringing while wood continues to shuffle and clack", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Bells_ringing_while_wood_continues.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Bells_ringing_while_wood_continues.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Bells_ringing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Wood_shuffling_and_clacking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Bells_ringing_while_wood_continues.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Muffled clock ticking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Muffled_clock_ticking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Muffled_clock_ticking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtTB0BK39JI8.wav"))
