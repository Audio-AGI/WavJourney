
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YvruDH_YLaPI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Gunfire, a burst of shots", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Gunfire_a_burst_of_shots.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Gunfire_a_burst_of_shots.wav")))

TTA(text="Magazine clinking sound", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Magazine_clinking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Magazine_clinking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Gunfire_a_burst_of_shots.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Magazine_clinking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YvruDH_YLaPI.wav"))
