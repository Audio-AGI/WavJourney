
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YYIqpIjjee00/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound effect of toilet flush lever pulled", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_effect_of_toilet_flush.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_effect_of_toilet_flush.wav")))

TTA(text="Sound effect of water rushing as the toilet bowl is refilling", length=7, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_effect_of_water_rushing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_effect_of_water_rushing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_effect_of_toilet_flush.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_effect_of_water_rushing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YYIqpIjjee00.wav"))
