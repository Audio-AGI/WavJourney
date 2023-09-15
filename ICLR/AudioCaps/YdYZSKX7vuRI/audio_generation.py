
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YdYZSKX7vuRI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="The sound of intense snoring", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_intense_snoring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_intense_snoring.wav")))

TTS(text="And then, John, a notorious sleep talker, begins his midnight monologue.", speaker_id="News_Male_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_And_then_John_a_notorious.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_And_then_John_a_notorious.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_intense_snoring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_And_then_John_a_notorious.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YdYZSKX7vuRI.wav"))
