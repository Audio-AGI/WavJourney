
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yo_3MDLl_aH0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Artillery cannon firing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Artillery_cannon_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Artillery_cannon_firing.wav")))

TTA(text="Artillery cannon firing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Artillery_cannon_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Artillery_cannon_firing.wav")))

TTA(text="Artillery cannon firing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Artillery_cannon_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Artillery_cannon_firing.wav")))

TTA(text="Artillery cannon firing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Artillery_cannon_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Artillery_cannon_firing.wav")))

TTA(text="Artillery cannon firing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Artillery_cannon_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Artillery_cannon_firing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Artillery_cannon_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Artillery_cannon_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Artillery_cannon_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Artillery_cannon_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Artillery_cannon_firing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yo_3MDLl_aH0.wav"))
