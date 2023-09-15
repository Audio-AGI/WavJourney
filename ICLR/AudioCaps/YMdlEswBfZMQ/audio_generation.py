
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMdlEswBfZMQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="People laughing cheerfully", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_People_laughing_cheerfully.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_People_laughing_cheerfully.wav")))

TTS(text="I wish I could laugh like that!", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_I_wish_I_could_laugh.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_wish_I_could_laugh.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_People_laughing_cheerfully.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_wish_I_could_laugh.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMdlEswBfZMQ.wav"))
