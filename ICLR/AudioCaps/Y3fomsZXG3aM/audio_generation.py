
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y3fomsZXG3aM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Idle vehicle engine running sound", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Idle_vehicle_engine_running_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Idle_vehicle_engine_running_sound.wav")))

TTA(text="Gear cranking sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Gear_cranking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Gear_cranking_sound.wav")))

TTA(text="Revving engine sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Revving_engine_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Revving_engine_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Idle_vehicle_engine_running_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Gear_cranking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Revving_engine_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y3fomsZXG3aM.wav"))
