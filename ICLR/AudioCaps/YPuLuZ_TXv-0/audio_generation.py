
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPuLuZ_TXv-0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Fast and sharp tap sounds of typewriter keys", length=7, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Fast_and_sharp_tap_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Fast_and_sharp_tap_sounds.wav")))

TTA(text="Intermittent zipping sound of the typewriter's carriage", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Intermittent_zipping_sound_of_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Intermittent_zipping_sound_of_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Fast_and_sharp_tap_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Intermittent_zipping_sound_of_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPuLuZ_TXv-0.wav"))
