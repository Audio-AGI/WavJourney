
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YXWw7ZM1c_QA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Surface scratching sound", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Surface_scratching_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Surface_scratching_sound.wav")))

TTA(text="ticktock sound", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_ticktock_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_ticktock_sound.wav")))

TTS(text="Words she is speaking while the sounds are being played.", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Words_she_is_speaking_while.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Words_she_is_speaking_while.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Surface_scratching_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_ticktock_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Words_she_is_speaking_while.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YXWw7ZM1c_QA.wav"))
