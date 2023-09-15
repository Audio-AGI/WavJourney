
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yq4YFJA5pFXc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Plastic clicking sound", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Plastic_clicking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clicking_sound.wav")))

TTA(text="Camera muffling sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Camera_muffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Camera_muffling_sound.wav")))

TTA(text="Toy helicopter motor sound starting up", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Toy_helicopter_motor_sound_starting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Toy_helicopter_motor_sound_starting.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clicking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Camera_muffling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Toy_helicopter_motor_sound_starting.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yq4YFJA5pFXc.wav"))
