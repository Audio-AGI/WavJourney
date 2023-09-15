
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yt1hj7se76wQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rapid typing on a keyboard", length=9.5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rapid_typing_on_a_keyboard.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rapid_typing_on_a_keyboard.wav")))

TTA(text="A single, sharp ding sound", length=0.5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_single_sharp_ding_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_single_sharp_ding_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rapid_typing_on_a_keyboard.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_single_sharp_ding_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yt1hj7se76wQ.wav"))
