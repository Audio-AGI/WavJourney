
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YcFoXRmGgIME/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="High pitches squealing", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_High_pitches_squealing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_High_pitches_squealing.wav")))

TTA(text="A horn blowing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_horn_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_horn_blowing.wav")))

TTA(text="Continuation of high pitches squealing", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Continuation_of_high_pitches_squealing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Continuation_of_high_pitches_squealing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_High_pitches_squealing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_horn_blowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Continuation_of_high_pitches_squealing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Constant humming of an engine", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Constant_humming_of_an_engine.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Constant_humming_of_an_engine.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YcFoXRmGgIME.wav"))
