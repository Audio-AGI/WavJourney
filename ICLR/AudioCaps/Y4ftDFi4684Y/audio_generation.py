
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4ftDFi4684Y/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Footsteps shuffling on a wooden floor", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_a_wooden.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_a_wooden.wav")))

TTA(text="Wooden door softly opening", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Wooden_door_softly_opening.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Wooden_door_softly_opening.wav")))

TTA(text="Clock ticking sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Clock_ticking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_a_wooden.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Wooden_door_softly_opening.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Clock_ticking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4ftDFi4684Y.wav"))
