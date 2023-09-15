
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YARFFw0e_jig/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud burping sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_burping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_burping_sound.wav")))

TTA(text="High pitched screaming sound", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_High_pitched_screaming_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_screaming_sound.wav")))

TTA(text="Silence", length=3, volume=-35, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Silence.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_burping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_screaming_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Silence.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YARFFw0e_jig.wav"))
