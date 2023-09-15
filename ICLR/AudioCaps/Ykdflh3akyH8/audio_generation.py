
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ykdflh3akyH8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Small dog yips", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Small_dog_yips.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Small_dog_yips.wav")))

TTA(text="Small dog whimpers", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Small_dog_whimpers.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Small_dog_whimpers.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Small_dog_yips.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Small_dog_whimpers.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ykdflh3akyH8.wav"))
