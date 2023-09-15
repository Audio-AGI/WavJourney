
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YnmLMLgWPmFM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="The engine seems to be in an excellent working condition.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_The_engine_seems_to_be.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_engine_seems_to_be.wav")))

TTS(text="Yes, the performance is truly impressive.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_the_performance_is_truly.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_the_performance_is_truly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_engine_seems_to_be.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_the_performance_is_truly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Soft humming of an engine", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Soft_humming_of_an_engine.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Soft_humming_of_an_engine.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YnmLMLgWPmFM.wav"))
