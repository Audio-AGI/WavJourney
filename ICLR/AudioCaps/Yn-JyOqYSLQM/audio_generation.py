
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yn-JyOqYSLQM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Heavy metal clanking", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Heavy_metal_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Heavy_metal_clanking.wav")))

TTA(text="Plastic rattling", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_rattling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_rattling.wav")))

TTA(text="Compressed air spraying", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Compressed_air_spraying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Compressed_air_spraying.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Heavy_metal_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_rattling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Compressed_air_spraying.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Indistinct chatter from a crowd of people in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Indistinct_chatter_from_a_crowd.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Indistinct_chatter_from_a_crowd.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yn-JyOqYSLQM.wav"))
