
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YfYTZVxQ8LJk/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="What a lovely day today.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_lovely_day_today.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_lovely_day_today.wav")))

TTS(text="Yeah, it's so sunny and bright.", speaker_id="Child_En", volume=-30, out_wav=os.path.join(wav_path, "fg_speech_1_Yeah_its_so_sunny_and.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yeah_its_so_sunny_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_lovely_day_today.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yeah_its_so_sunny_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YfYTZVxQ8LJk.wav"))
