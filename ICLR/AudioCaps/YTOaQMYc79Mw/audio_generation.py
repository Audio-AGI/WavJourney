
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YTOaQMYc79Mw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Motor vehicle engine clicks and whirs, trying to start", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Motor_vehicle_engine_clicks_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Motor_vehicle_engine_clicks_and.wav")))

TTA(text="Motor vehicle engine clicks and whirs, struggling to start for the second time", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Motor_vehicle_engine_clicks_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Motor_vehicle_engine_clicks_and.wav")))

TTA(text="Motor vehicle engine clicks and whirs, failing to start for the third time", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Motor_vehicle_engine_clicks_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Motor_vehicle_engine_clicks_and.wav")))

TTA(text="Soft metal clinking sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Soft_metal_clinking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Soft_metal_clinking_sound.wav")))

TTA(text="Deep buzzing sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Deep_buzzing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Deep_buzzing_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Motor_vehicle_engine_clicks_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Motor_vehicle_engine_clicks_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Motor_vehicle_engine_clicks_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Soft_metal_clinking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Deep_buzzing_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YTOaQMYc79Mw.wav"))
