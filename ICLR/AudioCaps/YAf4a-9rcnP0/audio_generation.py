
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YAf4a-9rcnP0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud burst sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_burst_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_burst_sound.wav")))

TTA(text="Rustling sound", length=4, volume=-21, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Rustling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Rustling_sound.wav")))

TTA(text="Sound of liquid spraying", length=3, volume=-19, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_liquid_spraying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_liquid_spraying.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_burst_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Rustling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_liquid_spraying.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YAf4a-9rcnP0.wav"))
