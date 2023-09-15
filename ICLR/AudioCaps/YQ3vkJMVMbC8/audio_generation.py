
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YQ3vkJMVMbC8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Toilet flushing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Toilet_flushing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Toilet_flushing.wav")))

TTA(text="Another toilet flushing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Another_toilet_flushing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Another_toilet_flushing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Toilet_flushing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Another_toilet_flushing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Infant shouting in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Infant_shouting_in_the_distance.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Infant_shouting_in_the_distance.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YQ3vkJMVMbC8.wav"))
