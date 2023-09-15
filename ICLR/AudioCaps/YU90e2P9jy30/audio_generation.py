
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YU90e2P9jy30/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of squeaking and bouncing, like a rubber ball being played with", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_squeaking_and_bouncing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_squeaking_and_bouncing.wav")))

TTS(text="That was fun, wasn't it?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_That_was_fun_wasnt_it.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_That_was_fun_wasnt_it.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_squeaking_and_bouncing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_That_was_fun_wasnt_it.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YU90e2P9jy30.wav"))
