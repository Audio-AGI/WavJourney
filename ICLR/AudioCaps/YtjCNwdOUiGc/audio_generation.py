
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtjCNwdOUiGc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Engine rumbling loudly", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Engine_rumbling_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Engine_rumbling_loudly.wav")))

TTA(text="Air horn honk", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Air_horn_honk.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Air_horn_honk.wav")))

TTA(text="Air horn honk", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Air_horn_honk.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Air_horn_honk.wav")))

TTA(text="Air horn honk", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Air_horn_honk.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Air_horn_honk.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Engine_rumbling_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Air_horn_honk.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Air_horn_honk.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Air_horn_honk.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtjCNwdOUiGc.wav"))
