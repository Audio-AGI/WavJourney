
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ye4ph6bIC5zc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Distant chattering human voices", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Distant_chattering_human_voices.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Distant_chattering_human_voices.wav")))

TTA(text="Sounds of a vehicle moving, motor running, and tires rolling", length=7, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sounds_of_a_vehicle_moving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sounds_of_a_vehicle_moving.wav")))

TTA(text="Distant chattering human voices fading out", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Distant_chattering_human_voices_fading.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Distant_chattering_human_voices_fading.wav")))

TTA(text="Sounds of a vehicle moving, motor running, and tires rolling on highway", length=7, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sounds_of_a_vehicle_moving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sounds_of_a_vehicle_moving.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Distant_chattering_human_voices.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sounds_of_a_vehicle_moving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Distant_chattering_human_voices_fading.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sounds_of_a_vehicle_moving.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Background city hum", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Background_city_hum.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Background_city_hum.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ye4ph6bIC5zc.wav"))
