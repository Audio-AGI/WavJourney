
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YROootH-mtEI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Water gently splashing against rocks", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Water_gently_splashing_against_rocks.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Water_gently_splashing_against_rocks.wav")))

TTA(text="Rustle of leaves in the wind and an occasional distant bird call", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Rustle_of_leaves_in_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Rustle_of_leaves_in_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Water_gently_splashing_against_rocks.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Rustle_of_leaves_in_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="River stream with water flowing, birds chirping in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_River_stream_with_water_flowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_River_stream_with_water_flowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YROootH-mtEI.wav"))
