
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YLP_DzNUkAKY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Engine humming intensifies", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Engine_humming_intensifies.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Engine_humming_intensifies.wav")))

TTA(text="People speaking louder", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_People_speaking_louder.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_People_speaking_louder.wav")))

TTA(text="Hissing sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Hissing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Hissing_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Engine_humming_intensifies.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_People_speaking_louder.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Hissing_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Engine humming", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Engine_humming.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="People speaking in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_People_speaking_in_the_distance.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Engine_humming.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_People_speaking_in_the_distance.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YLP_DzNUkAKY.wav"))
