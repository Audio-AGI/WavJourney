
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y8ZH_PoK0clI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rustling of clothes and objects", length=6, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rustling_of_clothes_and_objects.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rustling_of_clothes_and_objects.wav")))

TTA(text="Footsteps on a hard surface", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Footsteps_on_a_hard_surface.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Footsteps_on_a_hard_surface.wav")))

TTA(text="Continuation of rustling and footsteps", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Continuation_of_rustling_and_footsteps.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Continuation_of_rustling_and_footsteps.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rustling_of_clothes_and_objects.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Footsteps_on_a_hard_surface.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Continuation_of_rustling_and_footsteps.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Brief gasping of people, showing surprise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Brief_gasping_of_people_showing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Brief_gasping_of_people_showing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y8ZH_PoK0clI.wav"))
