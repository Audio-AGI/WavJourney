
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7XXSOzDQ2z0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Clicking sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound.wav")))

TTA(text="Sound of engines booming and accelerating into the distance", length=8, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_engines_booming_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_engines_booming_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_engines_booming_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7XXSOzDQ2z0.wav"))
