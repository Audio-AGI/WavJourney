
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YC9NC7wJ7C3w/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I speak very quickly and continuously for 10 seconds without taking a significant pause", speaker_id="Female2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_I_speak_very_quickly_and.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_speak_very_quickly_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_speak_very_quickly_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YC9NC7wJ7C3w.wav"))
