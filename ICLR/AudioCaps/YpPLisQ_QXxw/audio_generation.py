
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpPLisQ_QXxw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="High pitched horn honking", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_High_pitched_horn_honking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_High_pitched_horn_honking.wav")))

TTA(text="High pitched horn honking", length=8, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_High_pitched_horn_honking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_horn_honking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_High_pitched_horn_honking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_horn_honking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Vibrations of passing traffic", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Vibrations_of_passing_traffic.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Vibrations_of_passing_traffic.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpPLisQ_QXxw.wav"))
