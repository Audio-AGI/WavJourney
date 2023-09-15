
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YszkiW0GXEOI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Someone whistles", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Someone_whistles.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Someone_whistles.wav")))

TTA(text="Single bird tweeting", length=1, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Single_bird_tweeting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Single_bird_tweeting.wav")))

TTA(text="Silence", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Silence.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Someone_whistles.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Single_bird_tweeting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Silence.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Multiple birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Multiple_birds_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Multiple_birds_chirping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YszkiW0GXEOI.wav"))
