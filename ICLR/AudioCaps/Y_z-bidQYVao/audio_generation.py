
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_z-bidQYVao/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Horn sound similar to a car horn", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Horn_sound_similar_to_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Horn_sound_similar_to_a.wav")))

TTS(text="That was a horn sound. Sometimes, it is necessary to use it for alerting others.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_That_was_a_horn_sound.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_That_was_a_horn_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Horn_sound_similar_to_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_That_was_a_horn_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_z-bidQYVao.wav"))
