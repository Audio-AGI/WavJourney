
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9_YfTz8cnFY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Consistent hissing sounds", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Consistent_hissing_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Consistent_hissing_sounds.wav")))

TTA(text="Steam whistle blowing", length=6, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Steam_whistle_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Steam_whistle_blowing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Consistent_hissing_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Steam_whistle_blowing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Murmuring of people speaking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Murmuring_of_people_speaking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Murmuring_of_people_speaking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9_YfTz8cnFY.wav"))
