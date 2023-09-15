
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPvWI4p74UOs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Man laughing", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_laughing.wav")))

TTA(text="Birds chirping", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Distant humming sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_humming_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_humming_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPvWI4p74UOs.wav"))
