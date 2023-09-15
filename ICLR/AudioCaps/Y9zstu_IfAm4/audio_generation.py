
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9zstu_IfAm4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Engine revving sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Engine_revving_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Engine_revving_sound.wav")))

TTA(text="Horn honking sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Horn_honking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Horn_honking_sound.wav")))

TTA(text="More engine revving sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_More_engine_revving_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_More_engine_revving_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Engine_revving_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Horn_honking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_More_engine_revving_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9zstu_IfAm4.wav"))
