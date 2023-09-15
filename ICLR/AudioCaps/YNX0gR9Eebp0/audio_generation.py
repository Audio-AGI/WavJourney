
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YNX0gR9Eebp0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Water splashing sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Water_splashing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Water_splashing_sound.wav")))

TTS(text="Welcome to the world of audio scripts. Please, sit back and enjoy.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Welcome_to_the_world_of.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Welcome_to_the_world_of.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Water_splashing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Welcome_to_the_world_of.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YNX0gR9Eebp0.wav"))
