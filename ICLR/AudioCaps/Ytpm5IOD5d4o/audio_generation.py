
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ytpm5IOD5d4o/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, sit back and enjoy the tune.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_sit_back_and_enjoy.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_sit_back_and_enjoy.wav")))

TTA(text="A cheerful tune being whistled", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_cheerful_tune_being_whistled.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_cheerful_tune_being_whistled.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_sit_back_and_enjoy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_cheerful_tune_being_whistled.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ytpm5IOD5d4o.wav"))
