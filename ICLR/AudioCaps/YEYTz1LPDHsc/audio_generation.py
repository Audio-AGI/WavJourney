
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YEYTz1LPDHsc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle door opens", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_door_opens.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_door_opens.wav")))

TTA(text="A crow cawing", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_crow_cawing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_crow_cawing.wav")))

TTA(text="Birds chirping", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Birds_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Birds_chirping.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_door_opens.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_crow_cawing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Birds_chirping.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Cars moving, occasional car horns", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Cars_moving_occasional_car_horns.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Cars_moving_occasional_car_horns.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YEYTz1LPDHsc.wav"))
