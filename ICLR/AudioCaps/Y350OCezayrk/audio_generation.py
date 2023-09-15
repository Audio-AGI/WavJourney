
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y350OCezayrk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle door opening sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_door_opening_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_door_opening_sound.wav")))

TTA(text="Sitting on the vehicle's seat sound", length=1, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sitting_on_the_vehicles_seat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sitting_on_the_vehicles_seat.wav")))

TTA(text="Inserting the key into ignition sound", length=2, volume=-22, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Inserting_the_key_into_ignition.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Inserting_the_key_into_ignition.wav")))

TTA(text="Engine starting and running sound", length=5, volume=-16, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Engine_starting_and_running_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Engine_starting_and_running_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_door_opening_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sitting_on_the_vehicles_seat.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Inserting_the_key_into_ignition.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Engine_starting_and_running_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y350OCezayrk.wav"))
