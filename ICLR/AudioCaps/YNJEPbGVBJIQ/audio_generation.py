
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YNJEPbGVBJIQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Revving engines from a distance", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Revving_engines_from_a_distance.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Revving_engines_from_a_distance.wav")))

TTS(text="I always find this traffic chaos frustrating!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_I_always_find_this_traffic.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_always_find_this_traffic.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Revving_engines_from_a_distance.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_always_find_this_traffic.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Traffic hums, cars passing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Traffic_hums_cars_passing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Periodic beeping sounds from traffic light for pedestrians", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Periodic_beeping_sounds_from_traffic.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Traffic_hums_cars_passing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Periodic_beeping_sounds_from_traffic.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YNJEPbGVBJIQ.wav"))
