
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YVE6Ku0-ucUM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Did you know, a human can make over 10 different types of laughter?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Did_you_know_a_human.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Did_you_know_a_human.wav")))

TTA(text="Pop sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Pop_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Pop_sound.wav")))

TTA(text="Laughter sound", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughter_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughter_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Did_you_know_a_human.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Pop_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughter_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YVE6Ku0-ucUM.wav"))
