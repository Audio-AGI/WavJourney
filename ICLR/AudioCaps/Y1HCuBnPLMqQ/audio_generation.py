
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1HCuBnPLMqQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Plastic clacking sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_sound.wav")))

TTA(text="Person breathing heavily", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Person_breathing_heavily.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Person_breathing_heavily.wav")))

TTA(text="Sound of liquid pouring into containers", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_liquid_pouring_into.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_liquid_pouring_into.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Person_breathing_heavily.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_liquid_pouring_into.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1HCuBnPLMqQ.wav"))
