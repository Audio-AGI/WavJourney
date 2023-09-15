
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ycz0FSQDVBMw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Intermittent hissing", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Intermittent_hissing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Intermittent_hissing.wav")))

TTA(text="Intermittent clanking", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Intermittent_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Intermittent_clanking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Intermittent_hissing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Intermittent_clanking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous hissing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_hissing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Clanking sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Clanking_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_hissing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Clanking_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ycz0FSQDVBMw.wav"))
