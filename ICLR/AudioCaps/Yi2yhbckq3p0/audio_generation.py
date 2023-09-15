
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yi2yhbckq3p0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A typical motorcycle engine roaring for 10 seconds, overlaid with various car horns honking intermittently, and a car alarm goes off frequently", length=10, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_typical_motorcycle_engine_roaring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_typical_motorcycle_engine_roaring.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_typical_motorcycle_engine_roaring.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Motorbike engine running continuously", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Motorbike_engine_running_continuously.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Series of different vehicle horns sounding intermittently", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Series_of_different_vehicle_horns.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Car alarm sound looping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Car_alarm_sound_looping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Motorbike_engine_running_continuously.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Series_of_different_vehicle_horns.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Car_alarm_sound_looping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yi2yhbckq3p0.wav"))
