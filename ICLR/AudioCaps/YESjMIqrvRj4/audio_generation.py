
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YESjMIqrvRj4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Thunder sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Thunder_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Thunder_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Thunder_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Rain falling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Rain_falling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Birds_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Rain_falling.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Birds_chirping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YESjMIqrvRj4.wav"))
