
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YinQOrxc_oZo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Person shifting and moving", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Person_shifting_and_moving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Person_shifting_and_moving.wav")))

TTA(text="Subtle murmuring", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Subtle_murmuring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Subtle_murmuring.wav")))

TTA(text="Person screaming", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Person_screaming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Person_screaming.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Person_shifting_and_moving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Subtle_murmuring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Person_screaming.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YinQOrxc_oZo.wav"))
