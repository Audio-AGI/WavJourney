
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YZUmZgPL0ges/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A single church bell rings", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_single_church_bell_rings.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_single_church_bell_rings.wav")))

TTA(text="Two church bells ring in harmony", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Two_church_bells_ring_in.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Two_church_bells_ring_in.wav")))

TTA(text="Multiple church bells ringing together", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Multiple_church_bells_ringing_together.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Multiple_church_bells_ringing_together.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_single_church_bell_rings.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Two_church_bells_ring_in.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Multiple_church_bells_ringing_together.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YZUmZgPL0ges.wav"))
