
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y11SEBDuoqSk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Increase in the volume of aircraft engine sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Increase_in_the_volume_of.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Increase_in_the_volume_of.wav")))

TTA(text="Rapid gunshots firing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Rapid_gunshots_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Rapid_gunshots_firing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Increase_in_the_volume_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Rapid_gunshots_firing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous sound of an aircraft engine", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_sound_of_an_aircraft.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_sound_of_an_aircraft.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y11SEBDuoqSk.wav"))
