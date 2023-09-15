
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YrUq4w4EUSWA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud buzzing sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_buzzing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_buzzing_sound.wav")))

TTA(text="Sound of rustling", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_rustling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_rustling.wav")))

TTA(text="Sound of a toilet flushing", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_toilet_flushing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_toilet_flushing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_buzzing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_rustling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_toilet_flushing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YrUq4w4EUSWA.wav"))
