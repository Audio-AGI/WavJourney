
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-CcGuq0yoKo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Microphone feedback sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Microphone_feedback_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Microphone_feedback_sound.wav")))

TTS(text="Good evening, this is your host speaking. Thank you for joining us today.", speaker_id="News_Female_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Good_evening_this_is_your.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Good_evening_this_is_your.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Microphone_feedback_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Good_evening_this_is_your.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTM(text="Soft piano music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Soft_piano_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Soft_piano_music.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-CcGuq0yoKo.wav"))
