
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2JutOgAnqWA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Humming and vibrating of power tool", length=8, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Humming_and_vibrating_of_power.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Humming_and_vibrating_of_power.wav")))

TTA(text="High frequency squealing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_High_frequency_squealing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_High_frequency_squealing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Humming_and_vibrating_of_power.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_High_frequency_squealing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2JutOgAnqWA.wav"))
