
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YWmDe2xbnSY4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sharp burst sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sharp_burst_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sharp_burst_sound.wav")))

TTA(text="Powerful explosion sound", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Powerful_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Powerful_explosion_sound.wav")))

TTA(text="Low pitch grunting sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Low_pitch_grunting_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Low_pitch_grunting_sound.wav")))

TTA(text="Aggressive growling sound", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Aggressive_growling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Aggressive_growling_sound.wav")))

TTA(text="Loud explosion sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Loud_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Loud_explosion_sound.wav")))

TTA(text="Intense burst sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Intense_burst_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Intense_burst_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sharp_burst_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Powerful_explosion_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Low_pitch_grunting_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Aggressive_growling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Loud_explosion_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Intense_burst_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YWmDe2xbnSY4.wav"))
