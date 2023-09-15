
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YoZaEHkfh5Eg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle horn honking", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_horn_honking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_horn_honking.wav")))

TTA(text="Series of electronic beeps", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Series_of_electronic_beeps.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Series_of_electronic_beeps.wav")))

TTA(text="Plastic clicking sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Plastic_clicking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Plastic_clicking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_horn_honking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Series_of_electronic_beeps.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Plastic_clicking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YoZaEHkfh5Eg.wav"))
