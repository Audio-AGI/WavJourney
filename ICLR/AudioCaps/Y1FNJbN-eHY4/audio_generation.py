
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1FNJbN-eHY4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A strong and slightly rude burp", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_strong_and_slightly_rude.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_strong_and_slightly_rude.wav")))

TTA(text="Lively and hearty laughter", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Lively_and_hearty_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Lively_and_hearty_laughter.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_strong_and_slightly_rude.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Lively_and_hearty_laughter.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1FNJbN-eHY4.wav"))
