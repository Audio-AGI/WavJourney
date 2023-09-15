
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YW7OJevEgq7w/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A dog panting", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_dog_panting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_dog_panting.wav")))

TTA(text="A dog barking", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_dog_barking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_dog_barking.wav")))

TTA(text="A dog yipping", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_A_dog_yipping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_A_dog_yipping.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_dog_panting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_dog_barking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_A_dog_yipping.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YW7OJevEgq7w.wav"))
