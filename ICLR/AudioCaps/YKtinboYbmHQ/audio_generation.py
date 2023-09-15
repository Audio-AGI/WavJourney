
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YKtinboYbmHQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle engine sound starting and revving", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_sound_starting_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_sound_starting_and.wav")))

TTA(text="Vehicle driving by", length=4, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Vehicle_driving_by.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_driving_by.wav")))

TTA(text="Tires skidding sound", length=4, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Tires_skidding_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Tires_skidding_sound.wav")))

TTA(text="Tires squealing sound as the vehicle drives away", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Tires_squealing_sound_as_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Tires_squealing_sound_as_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_sound_starting_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_driving_by.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Tires_skidding_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Tires_squealing_sound_as_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YKtinboYbmHQ.wav"))
