
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y63KW_EQ72yU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Intense explosion sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Intense_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Intense_explosion_sound.wav")))

TTA(text="Sound of debris rattling, fading gradually", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_debris_rattling_fading.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_debris_rattling_fading.wav")))

TTA(text="Second intense explosion sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Second_intense_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Second_intense_explosion_sound.wav")))

TTA(text="Sound of debris rattling, fading gradually", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sound_of_debris_rattling_fading.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_debris_rattling_fading.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Intense_explosion_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_debris_rattling_fading.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Second_intense_explosion_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_debris_rattling_fading.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y63KW_EQ72yU.wav"))
