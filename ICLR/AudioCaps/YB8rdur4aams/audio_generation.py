
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YB8rdur4aams/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle engine gurgling", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_gurgling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_gurgling.wav")))

TTA(text="Horn tooting", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Horn_tooting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Horn_tooting.wav")))

TTA(text="Microphone picking up wind noise", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Microphone_picking_up_wind_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Microphone_picking_up_wind_noise.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_gurgling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Horn_tooting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Microphone_picking_up_wind_noise.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Wind blowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YB8rdur4aams.wav"))
