
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpaetCbEqp2w/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="successive computer mouse clicks", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_successive_computer_mouse_clicks.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_successive_computer_mouse_clicks.wav")))

TTA(text="a kid crying", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_a_kid_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_a_kid_crying.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_successive_computer_mouse_clicks.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_a_kid_crying.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpaetCbEqp2w.wav"))
