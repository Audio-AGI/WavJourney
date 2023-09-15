
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFA11v4SmdBc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Listen closely, I'm going to whistle a tune for you.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Listen_closely_Im_going_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Listen_closely_Im_going_to.wav")))

TTA(text="Man whistling a catchy tune", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_catchy_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_catchy_tune.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Listen_closely_Im_going_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_catchy_tune.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFA11v4SmdBc.wav"))
