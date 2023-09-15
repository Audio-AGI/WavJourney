
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YjjfUaMQaG1A/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Let's get started with the tool.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Lets_get_started_with_the.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Lets_get_started_with_the.wav")))

TTA(text="Vibrations of a power tool", length=8, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vibrations_of_a_power_tool.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vibrations_of_a_power_tool.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Lets_get_started_with_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vibrations_of_a_power_tool.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YjjfUaMQaG1A.wav"))
