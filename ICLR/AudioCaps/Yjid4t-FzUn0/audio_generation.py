
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yjid4t-FzUn0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello there! I'm so happy today.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_there_Im_so_happy.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_there_Im_so_happy.wav")))

TTA(text="Man laughing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_laughing.wav")))

TTA(text="Goat bleating", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Goat_bleating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Goat_bleating.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_there_Im_so_happy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Goat_bleating.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yjid4t-FzUn0.wav"))
