
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBn4lc01q9vE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Water splashing sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Water_splashing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Water_splashing_sound.wav")))

TTS(text="What a refreshing swim.", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_refreshing_swim.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_refreshing_swim.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Water_splashing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_refreshing_swim.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBn4lc01q9vE.wav"))
