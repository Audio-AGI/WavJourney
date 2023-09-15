
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YQHfyKaOHSz4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a fly buzzing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_fly_buzzing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_fly_buzzing.wav")))

TTA(text="Sound of a frog swallowing", length=2, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_frog_swallowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_frog_swallowing.wav")))

TTA(text="Frog croaking sound", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Frog_croaking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Frog_croaking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_fly_buzzing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_frog_swallowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Frog_croaking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YQHfyKaOHSz4.wav"))
