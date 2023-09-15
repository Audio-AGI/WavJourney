
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_C2HinL8VlM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Two blasts of a police car's horn", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Two_blasts_of_a_police.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Two_blasts_of_a_police.wav")))

TTA(text="High pitched wail of a police car siren", length=8, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_High_pitched_wail_of_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_wail_of_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Two_blasts_of_a_police.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_wail_of_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_C2HinL8VlM.wav"))
