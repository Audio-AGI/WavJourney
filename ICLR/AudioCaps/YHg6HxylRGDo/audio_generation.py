
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHg6HxylRGDo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="The blaring siren of an ambulance", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_blaring_siren_of_an.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_blaring_siren_of_an.wav")))

TTA(text="A vehicle revving up loudly", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_vehicle_revving_up_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_vehicle_revving_up_loudly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_blaring_siren_of_an.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_vehicle_revving_up_loudly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHg6HxylRGDo.wav"))
