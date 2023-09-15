
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YVeCSHwtkBZU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Siren of an emergency vehicle", length=10, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Siren_of_an_emergency_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Siren_of_an_emergency_vehicle.wav")))

TTA(text="Tires screeching on asphalt as vehicle accelerates", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Tires_screeching_on_asphalt_as.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Tires_screeching_on_asphalt_as.wav")))

TTA(text="Vehicle rushing past with the doppler effect", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Vehicle_rushing_past_with_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Vehicle_rushing_past_with_the.wav")))

TTA(text="Distant siren trailing off into the night. Siren echoes, slightly muffled", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Distant_siren_trailing_off_into.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Distant_siren_trailing_off_into.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Siren_of_an_emergency_vehicle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Tires_screeching_on_asphalt_as.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Vehicle_rushing_past_with_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Distant_siren_trailing_off_into.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:4])
bg_audio_offset = sum(fg_audio_lens[:1])
TTM(text="Low volume suspenseful music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Low_volume_suspenseful_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Low_volume_suspenseful_music.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YVeCSHwtkBZU.wav"))
