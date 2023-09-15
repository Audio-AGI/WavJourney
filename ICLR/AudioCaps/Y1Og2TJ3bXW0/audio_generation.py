
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1Og2TJ3bXW0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Aircraft engine running", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Aircraft_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Aircraft_engine_running.wav")))

TTA(text="Plastic click sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_click_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_click_sound.wav")))

TTA(text="Aircraft engine slowing down", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Aircraft_engine_slowing_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Aircraft_engine_slowing_down.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Aircraft_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_click_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Aircraft_engine_slowing_down.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1Og2TJ3bXW0.wav"))
