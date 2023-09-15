
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y3wV3ST-c4PE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Low ticktock sounds", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Low_ticktock_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Low_ticktock_sounds.wav")))

TTA(text="Objects moving on a surface sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Objects_moving_on_a_surface.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Objects_moving_on_a_surface.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Low_ticktock_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Objects_moving_on_a_surface.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y3wV3ST-c4PE.wav"))
