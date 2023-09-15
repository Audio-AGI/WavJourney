
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2KR0C5ysO8o/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Mid-size motor vehicle engine accelerating", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Midsize_motor_vehicle_engine_accelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Midsize_motor_vehicle_engine_accelerating.wav")))

TTA(text="Hissing sound from the engine", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Hissing_sound_from_the_engine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Hissing_sound_from_the_engine.wav")))

TTA(text="Spinning tires on asphalt", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Spinning_tires_on_asphalt.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Spinning_tires_on_asphalt.wav")))

TTA(text="Mid-size motor vehicle engine decelerating", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Midsize_motor_vehicle_engine_decelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Midsize_motor_vehicle_engine_decelerating.wav")))

TTS(text="That was a nice ride.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_That_was_a_nice_ride.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_That_was_a_nice_ride.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Midsize_motor_vehicle_engine_accelerating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Hissing_sound_from_the_engine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Spinning_tires_on_asphalt.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Midsize_motor_vehicle_engine_decelerating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_That_was_a_nice_ride.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2KR0C5ysO8o.wav"))
