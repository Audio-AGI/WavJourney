
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMPLZUg89y5U/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="And here we are on site, the enormous vehicle idling in the background. We're not sure what to expect next.", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_And_here_we_are_on.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_And_here_we_are_on.wav")))

TTA(text="Microphone picks up gust of wind", length=0.5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Microphone_picks_up_gust_of.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Microphone_picks_up_gust_of.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_And_here_we_are_on.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Microphone_picks_up_gust_of.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Large truck engine running idle", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Large_truck_engine_running_idle.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of wind blowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Large_truck_engine_running_idle.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_wind_blowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMPLZUg89y5U.wav"))
