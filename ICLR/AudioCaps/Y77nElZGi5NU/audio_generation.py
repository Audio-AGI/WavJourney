
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y77nElZGi5NU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud party popper bursting sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_party_popper_bursting_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_party_popper_bursting_sound.wav")))

TTA(text="Peoples' cheerful laughter", length=7, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Peoples_cheerful_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Peoples_cheerful_laughter.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_party_popper_bursting_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Peoples_cheerful_laughter.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y77nElZGi5NU.wav"))
