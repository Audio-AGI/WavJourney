
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtJhVH3VIrnE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Wood cracking", length=7, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Wood_cracking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Wood_cracking.wav")))

TTA(text="Metal clanking", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_clanking.wav")))

TTA(text="Metal slamming against a wooden surface", length=10, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Metal_slamming_against_a_wooden.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Metal_slamming_against_a_wooden.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Wood_cracking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Metal_slamming_against_a_wooden.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtJhVH3VIrnE.wav"))
