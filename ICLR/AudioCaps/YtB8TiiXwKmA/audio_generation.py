
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtB8TiiXwKmA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vibrating sound of a power tool", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vibrating_sound_of_a_power.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vibrating_sound_of_a_power.wav")))

TTA(text="Humming sound of a power tool", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Humming_sound_of_a_power.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Humming_sound_of_a_power.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vibrating_sound_of_a_power.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Humming_sound_of_a_power.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtB8TiiXwKmA.wav"))
