
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yg5l3Bz6lWnc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Light wooden shuffling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Light_wooden_shuffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Light_wooden_shuffling_sound.wav")))

TTA(text="Light wooden shuffling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Light_wooden_shuffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Light_wooden_shuffling_sound.wav")))

TTA(text="Light wooden shuffling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Light_wooden_shuffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Light_wooden_shuffling_sound.wav")))

TTA(text="Light wooden shuffling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Light_wooden_shuffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Light_wooden_shuffling_sound.wav")))

TTA(text="Light wooden shuffling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Light_wooden_shuffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Light_wooden_shuffling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Light_wooden_shuffling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Light_wooden_shuffling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Light_wooden_shuffling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Light_wooden_shuffling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Light_wooden_shuffling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:5])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Insects buzzing quietly", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Insects_buzzing_quietly.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:5])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Birds chirping subtly", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Birds_chirping_subtly.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Insects_buzzing_quietly.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Birds_chirping_subtly.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yg5l3Bz6lWnc.wav"))
