
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCM49C3RkzV8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, how are you?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_how_are_you.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_how_are_you.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_how_are_you.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Muted speech in a busy environment", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Muted_speech_in_a_busy.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Muted_speech_in_a_busy.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCM49C3RkzV8.wav"))
