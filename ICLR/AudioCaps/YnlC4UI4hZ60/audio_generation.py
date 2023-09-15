
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YnlC4UI4hZ60/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rapid clicking sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rapid_clicking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rapid_clicking_sound.wav")))

TTA(text="Motor vehicle engine attempting to start, with grinding sounds", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Motor_vehicle_engine_attempting_to.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Motor_vehicle_engine_attempting_to.wav")))

TTA(text="Engine fully engages. It begins to run and vibrate", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Engine_fully_engages_It_begins.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Engine_fully_engages_It_begins.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rapid_clicking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Motor_vehicle_engine_attempting_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Engine_fully_engages_It_begins.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YnlC4UI4hZ60.wav"))
