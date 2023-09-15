
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YAWGnTI0e2Fs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="High frequency humming sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_High_frequency_humming_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_High_frequency_humming_sound.wav")))

TTA(text="Humming sound slowing down and stopping", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Humming_sound_slowing_down_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Humming_sound_slowing_down_and.wav")))

TTA(text="Humming sound starting and increasing frequency", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Humming_sound_starting_and_increasing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Humming_sound_starting_and_increasing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_High_frequency_humming_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Humming_sound_slowing_down_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Humming_sound_starting_and_increasing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YAWGnTI0e2Fs.wav"))
