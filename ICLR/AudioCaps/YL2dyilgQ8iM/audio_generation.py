
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YL2dyilgQ8iM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Footsteps shuffling on snow", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_snow.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_snow.wav")))

TTA(text="Sound of camera muffling", length=5, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_camera_muffling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_camera_muffling.wav")))

TTA(text="Footsteps shuffling on snow", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Footsteps_shuffling_on_snow.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Footsteps_shuffling_on_snow.wav")))

TTA(text="Sound of camera muffling", length=5, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sound_of_camera_muffling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_camera_muffling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_snow.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_camera_muffling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Footsteps_shuffling_on_snow.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_camera_muffling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of wind blowing into a microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_wind_blowing_into.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_wind_blowing_into.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YL2dyilgQ8iM.wav"))
