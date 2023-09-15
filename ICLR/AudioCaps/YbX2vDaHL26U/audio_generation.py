
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YbX2vDaHL26U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Strong wind blowing loudly", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Strong_wind_blowing_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Strong_wind_blowing_loudly.wav")))

TTA(text="Car accelerating fast", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Car_accelerating_fast.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Car_accelerating_fast.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Strong_wind_blowing_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Car_accelerating_fast.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YbX2vDaHL26U.wav"))
