
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFi4-IqJo2xQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle engine revving", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_revving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_revving.wav")))

TTA(text="Series of compressed air releasing", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Series_of_compressed_air_releasing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Series_of_compressed_air_releasing.wav")))

TTA(text="Plastic pops", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Plastic_pops.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Plastic_pops.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_revving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Series_of_compressed_air_releasing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Plastic_pops.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFi4-IqJo2xQ.wav"))
