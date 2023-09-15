
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YTwR8BA6buMI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a plastic object hitting a hard surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_plastic_object.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_plastic_object.wav")))

TTA(text="Sound of a plastic object hitting a hard surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_plastic_object.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_plastic_object.wav")))

TTA(text="Sound of a plastic object hitting a hard surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_plastic_object.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_plastic_object.wav")))

TTA(text="Sound of a plastic object hitting a hard surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sound_of_a_plastic_object.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_a_plastic_object.wav")))

TTA(text="Sound of a plastic object hitting a hard surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Sound_of_a_plastic_object.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Sound_of_a_plastic_object.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_plastic_object.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_plastic_object.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_plastic_object.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_a_plastic_object.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Sound_of_a_plastic_object.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:5])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Smooth, soothing piano music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Smooth_soothing_piano_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Smooth_soothing_piano_music.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YTwR8BA6buMI.wav"))
