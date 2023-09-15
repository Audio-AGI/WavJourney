
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YEBCH7TPgiPc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of vehicle accelerating", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_vehicle_accelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_vehicle_accelerating.wav")))

TTA(text="Sound of vehicle slowing down", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_vehicle_slowing_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_vehicle_slowing_down.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_vehicle_accelerating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_vehicle_slowing_down.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YEBCH7TPgiPc.wav"))
