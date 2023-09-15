
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YAR8-MVl_Mf8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Man screaming", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_screaming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_screaming.wav")))

TTA(text="Door slamming shut", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Door_slamming_shut.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Door_slamming_shut.wav")))

TTA(text="Cardboard thumping", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Cardboard_thumping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Cardboard_thumping.wav")))

TTA(text="Metal bars clacking", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Metal_bars_clacking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Metal_bars_clacking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_screaming.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Door_slamming_shut.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Cardboard_thumping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Metal_bars_clacking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YAR8-MVl_Mf8.wav"))
