
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4pf-PIymDhU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Jackhammer operating at a high rate", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Jackhammer_operating_at_a_high.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Jackhammer_operating_at_a_high.wav")))

TTA(text="Jackhammer slowing down", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Jackhammer_slowing_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Jackhammer_slowing_down.wav")))

TTA(text="Jackhammer operating at a normal rate", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Jackhammer_operating_at_a_normal.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Jackhammer_operating_at_a_normal.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Jackhammer_operating_at_a_high.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Jackhammer_slowing_down.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Jackhammer_operating_at_a_normal.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4pf-PIymDhU.wav"))
