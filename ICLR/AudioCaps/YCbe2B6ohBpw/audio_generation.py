
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCbe2B6ohBpw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A duck quacking repeatedly", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_duck_quacking_repeatedly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_duck_quacking_repeatedly.wav")))

TTA(text="Horse hooves clopping on a hard surface", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Horse_hooves_clopping_on_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Horse_hooves_clopping_on_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_duck_quacking_repeatedly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Horse_hooves_clopping_on_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCbe2B6ohBpw.wav"))
