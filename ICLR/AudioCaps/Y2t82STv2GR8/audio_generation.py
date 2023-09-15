
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2t82STv2GR8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="First bell ring", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_bell_ring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_bell_ring.wav")))

TTA(text="Second bell ring", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_bell_ring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_bell_ring.wav")))

TTA(text="Third bell ring", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Third_bell_ring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Third_bell_ring.wav")))

TTA(text="Fourth bell ring", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Fourth_bell_ring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Fourth_bell_ring.wav")))

TTA(text="Fifth bell ring", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Fifth_bell_ring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Fifth_bell_ring.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_bell_ring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_bell_ring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Third_bell_ring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Fourth_bell_ring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Fifth_bell_ring.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2t82STv2GR8.wav"))
