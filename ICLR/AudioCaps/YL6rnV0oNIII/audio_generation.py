
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YL6rnV0oNIII/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Electronic beeping sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Electronic_beeping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beeping_sound.wav")))

TTA(text="Plastic clicking sound", length=2, volume=-22, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_clicking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_clicking_sound.wav")))

TTA(text="Laser effect sound", length=3, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Laser_effect_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Laser_effect_sound.wav")))

TTA(text="Wooden thud sound", length=1.5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Wooden_thud_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Wooden_thud_sound.wav")))

TTA(text="Synthesized explosion sound", length=1.5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Synthesized_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Synthesized_explosion_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beeping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_clicking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Laser_effect_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Wooden_thud_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Synthesized_explosion_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YL6rnV0oNIII.wav"))
