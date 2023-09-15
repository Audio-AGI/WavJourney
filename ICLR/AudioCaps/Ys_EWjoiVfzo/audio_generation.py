
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ys_EWjoiVfzo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rustling sound of papers", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rustling_sound_of_papers.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rustling_sound_of_papers.wav")))

TTA(text="Soft humming sound", length=6, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Soft_humming_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Soft_humming_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rustling_sound_of_papers.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Soft_humming_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Consistent clicks in the background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Consistent_clicks_in_the_background.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Consistent_clicks_in_the_background.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ys_EWjoiVfzo.wav"))
