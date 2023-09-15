
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YAI1OweEW8C0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Wind blowing into a microphone", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Wind_blowing_into_a_microphone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Wind_blowing_into_a_microphone.wav")))

TTA(text="Thunder roaring in the distance", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Thunder_roaring_in_the_distance.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Thunder_roaring_in_the_distance.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Wind_blowing_into_a_microphone.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Thunder_roaring_in_the_distance.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Soft sound of stream water trickling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Soft_sound_of_stream_water.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Soft_sound_of_stream_water.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YAI1OweEW8C0.wav"))
