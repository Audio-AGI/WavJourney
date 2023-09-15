
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9xoYx3lTJ9I/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Speedboat sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Speedboat_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Speedboat_sound.wav")))

TTA(text="Water splashes", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Water_splashes.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Water_splashes.wav")))

TTS(text="Speed boat passes at fast pace", speaker_id="News_Male_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Speed_boat_passes_at_fast.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Speed_boat_passes_at_fast.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Speedboat_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Water_splashes.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Speed_boat_passes_at_fast.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing heavily", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing_heavily.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing_heavily.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9xoYx3lTJ9I.wav"))
