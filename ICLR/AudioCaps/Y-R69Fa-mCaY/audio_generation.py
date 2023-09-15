
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-R69Fa-mCaY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Chainsaw cutting sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Chainsaw_cutting_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Chainsaw_cutting_sound.wav")))

TTA(text="Wood cracking sound", length=5, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Wood_cracking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Wood_cracking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Chainsaw_cutting_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Wood_cracking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-R69Fa-mCaY.wav"))
