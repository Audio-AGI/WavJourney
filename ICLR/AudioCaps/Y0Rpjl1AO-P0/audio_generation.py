
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y0Rpjl1AO-P0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Car acceleration sound effect", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Car_acceleration_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Car_acceleration_sound_effect.wav")))

TTA(text="Sound of the car moving at a high speed", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_the_car_moving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_the_car_moving.wav")))

TTA(text="Sound of the car changing gears", length=3, volume=-22, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_the_car_changing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_the_car_changing.wav")))

TTA(text="Car deceleration sound effect", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Car_deceleration_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Car_deceleration_sound_effect.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Car_acceleration_sound_effect.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_the_car_moving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_the_car_changing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Car_deceleration_sound_effect.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Car engine revving sound effect", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Car_engine_revving_sound_effect.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Car_engine_revving_sound_effect.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y0Rpjl1AO-P0.wav"))
