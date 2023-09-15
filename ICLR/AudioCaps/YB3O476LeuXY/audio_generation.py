
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YB3O476LeuXY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Humming sound from an idling engine", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Humming_sound_from_an_idling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Humming_sound_from_an_idling.wav")))

TTA(text="Sputtering sounds from an idling engine", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sputtering_sounds_from_an_idling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sputtering_sounds_from_an_idling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Humming_sound_from_an_idling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sputtering_sounds_from_an_idling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YB3O476LeuXY.wav"))
