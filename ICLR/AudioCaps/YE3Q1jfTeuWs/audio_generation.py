
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YE3Q1jfTeuWs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Baby crying loudly", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_loudly.wav")))

TTA(text="Baby taking a deep breath", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Baby_taking_a_deep_breath.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Baby_taking_a_deep_breath.wav")))

TTA(text="Baby crying loudly", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Baby_crying_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Baby_crying_loudly.wav")))

TTA(text="Baby taking a deep breath", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Baby_taking_a_deep_breath.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Baby_taking_a_deep_breath.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Baby_taking_a_deep_breath.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Baby_crying_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Baby_taking_a_deep_breath.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTM(text="Faint sound of a lullaby being played in the background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Faint_sound_of_a_lullaby.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Faint_sound_of_a_lullaby.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YE3Q1jfTeuWs.wav"))
