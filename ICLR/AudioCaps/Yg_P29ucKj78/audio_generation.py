
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yg_P29ucKj78/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of keys jingling", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_keys_jingling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_keys_jingling.wav")))

TTA(text="Sound of a car door opening and closing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_car_door.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_car_door.wav")))

TTA(text="Sound of car engine starting", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_car_engine_starting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_car_engine_starting.wav")))

TTA(text="First gear shift sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_First_gear_shift_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_First_gear_shift_sound.wav")))

TTA(text="Second gear shift sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Second_gear_shift_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Second_gear_shift_sound.wav")))

TTA(text="Sound of car slowly coming to a halt", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Sound_of_car_slowly_coming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Sound_of_car_slowly_coming.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_keys_jingling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_car_door.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_car_engine_starting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_First_gear_shift_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Second_gear_shift_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Sound_of_car_slowly_coming.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:5])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Engine humming noise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Engine_humming_noise.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Engine_humming_noise.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yg_P29ucKj78.wav"))
