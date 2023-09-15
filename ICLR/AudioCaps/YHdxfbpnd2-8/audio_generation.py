
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHdxfbpnd2-8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's such a bright and beautiful day.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Its_such_a_bright_and.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_such_a_bright_and.wav")))

TTA(text="Man whistling a cheerful tune", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_cheerful_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_cheerful_tune.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_such_a_bright_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_cheerful_tune.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHdxfbpnd2-8.wav"))
