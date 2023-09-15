
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_xylo5_IiaM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, I hope you are having a great day today.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_I_hope_you_are.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_I_hope_you_are.wav")))

TTS(text="Goo goo ga ga", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Goo_goo_ga_ga.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Goo_goo_ga_ga.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_I_hope_you_are.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Goo_goo_ga_ga.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_xylo5_IiaM.wav"))
