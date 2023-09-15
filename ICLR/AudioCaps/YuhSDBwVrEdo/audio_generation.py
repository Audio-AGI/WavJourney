
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YuhSDBwVrEdo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Person whistling a tune", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Person_whistling_a_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Person_whistling_a_tune.wav")))

TTA(text="Person continues whistling", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Person_continues_whistling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Person_continues_whistling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Person_whistling_a_tune.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Person_continues_whistling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Gentle wind blowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Gentle_wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Gentle_wind_blowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YuhSDBwVrEdo.wav"))
