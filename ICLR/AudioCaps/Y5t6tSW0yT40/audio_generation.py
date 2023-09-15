
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y5t6tSW0yT40/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Clicking sound of a machine being turned on", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_of_a_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_of_a_machine.wav")))

TTA(text="Mechanical sound of machine preparing to spray", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Mechanical_sound_of_machine_preparing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Mechanical_sound_of_machine_preparing.wav")))

TTA(text="Spraying sound effect for an extended period", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Spraying_sound_effect_for_an.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Spraying_sound_effect_for_an.wav")))

TTA(text="Mechanical sound of machine being turned off after spraying", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Mechanical_sound_of_machine_being.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Mechanical_sound_of_machine_being.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_of_a_machine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Mechanical_sound_of_machine_preparing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Spraying_sound_effect_for_an.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Mechanical_sound_of_machine_being.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y5t6tSW0yT40.wav"))
