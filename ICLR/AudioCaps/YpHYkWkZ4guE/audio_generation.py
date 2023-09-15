
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpHYkWkZ4guE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Metal clanking", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Metal_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Metal_clanking.wav")))

TTA(text="Gears cranking", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Gears_cranking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Gears_cranking.wav")))

TTA(text="Metal clanking", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Metal_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Metal_clanking.wav")))

TTA(text="Gears cranking", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Gears_cranking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Gears_cranking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Metal_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Gears_cranking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Metal_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Gears_cranking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Continuous steam hissing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_steam_hissing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_steam_hissing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpHYkWkZ4guE.wav"))
