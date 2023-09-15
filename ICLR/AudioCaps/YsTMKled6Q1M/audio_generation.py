
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YsTMKled6Q1M/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of light rough materials such as paper or leaves rustling", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_light_rough_materials.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_light_rough_materials.wav")))

TTA(text="Whistling sound resembling the tune a person would whistle", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Whistling_sound_resembling_the_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Whistling_sound_resembling_the_tune.wav")))

TTA(text="Melodious chirping of birds, typically heard in a forest", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Melodious_chirping_of_birds_typically.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Melodious_chirping_of_birds_typically.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_light_rough_materials.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Whistling_sound_resembling_the_tune.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Melodious_chirping_of_birds_typically.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YsTMKled6Q1M.wav"))
