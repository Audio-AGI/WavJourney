
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YcN-oYKd-M4E/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Close sheep bleat", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Close_sheep_bleat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Close_sheep_bleat.wav")))

TTA(text="Close sheep bleat", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Close_sheep_bleat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Close_sheep_bleat.wav")))

TTA(text="Close sheep bleat", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Close_sheep_bleat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Close_sheep_bleat.wav")))

TTA(text="Close sheep bleat", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Close_sheep_bleat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Close_sheep_bleat.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Close_sheep_bleat.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Close_sheep_bleat.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Close_sheep_bleat.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Close_sheep_bleat.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:3])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Distant sheep bleats", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_sheep_bleats.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_sheep_bleats.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YcN-oYKd-M4E.wav"))
