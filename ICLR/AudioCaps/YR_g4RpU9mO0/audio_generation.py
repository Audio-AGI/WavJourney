
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YR_g4RpU9mO0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Boat motor idling sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Boat_motor_idling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Boat_motor_idling_sound.wav")))

TTA(text="Boat motor accelerating sound", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Boat_motor_accelerating_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Boat_motor_accelerating_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Boat_motor_idling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Boat_motor_accelerating_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YR_g4RpU9mO0.wav"))
