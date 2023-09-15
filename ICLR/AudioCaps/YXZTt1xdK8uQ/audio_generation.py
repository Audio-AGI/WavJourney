
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YXZTt1xdK8uQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle engine starting and idling", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_starting_and_idling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_starting_and_idling.wav")))

TTA(text="Vehicle engine accelerating with a loud exhaust", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Vehicle_engine_accelerating_with_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_engine_accelerating_with_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_starting_and_idling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_engine_accelerating_with_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous water gurgling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_water_gurgling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_water_gurgling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YXZTt1xdK8uQ.wav"))
