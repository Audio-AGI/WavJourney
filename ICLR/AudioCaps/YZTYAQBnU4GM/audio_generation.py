
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YZTYAQBnU4GM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="First bird chirping", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_bird_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_bird_chirping.wav")))

TTA(text="Second bird chirping", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_bird_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_bird_chirping.wav")))

TTA(text="Third bird chirping", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Third_bird_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Third_bird_chirping.wav")))

TTA(text="Fourth bird chirping", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Fourth_bird_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Fourth_bird_chirping.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_bird_chirping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_bird_chirping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Third_bird_chirping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Fourth_bird_chirping.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YZTYAQBnU4GM.wav"))
