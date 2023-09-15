
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YsqWyxUObwkw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a key turn", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_key_turn.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_key_turn.wav")))

TTA(text="Motorboat engine starting and slowly coming to life", length=8, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Motorboat_engine_starting_and_slowly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Motorboat_engine_starting_and_slowly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_key_turn.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Motorboat_engine_starting_and_slowly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YsqWyxUObwkw.wav"))
