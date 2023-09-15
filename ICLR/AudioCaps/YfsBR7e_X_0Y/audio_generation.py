
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YfsBR7e_X_0Y/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Yaaahhhh! Yaaahhhh! Yaaahhhh!", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Yaaahhhh_Yaaahhhh_Yaaahhhh.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Yaaahhhh_Yaaahhhh_Yaaahhhh.wav")))

TTS(text="Hey, stop! Cut it out!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Hey_stop_Cut_it_out.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hey_stop_Cut_it_out.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Yaaahhhh_Yaaahhhh_Yaaahhhh.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hey_stop_Cut_it_out.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of several slaps on a hard surface", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_several_slaps_on.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_several_slaps_on.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YfsBR7e_X_0Y.wav"))
