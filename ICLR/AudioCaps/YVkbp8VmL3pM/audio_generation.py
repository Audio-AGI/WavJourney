
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YVkbp8VmL3pM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Baby crying loudly", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_loudly.wav")))

TTA(text="Brief silence", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Brief_silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Brief_silence.wav")))

TTA(text="Baby shouting", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Baby_shouting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Baby_shouting.wav")))

TTA(text="Sounds of baby cooing softly", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sounds_of_baby_cooing_softly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sounds_of_baby_cooing_softly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Brief_silence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Baby_shouting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sounds_of_baby_cooing_softly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YVkbp8VmL3pM.wav"))
