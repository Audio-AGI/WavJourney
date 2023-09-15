
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2ymiXjImwGs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Siren blaring far away", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Siren_blaring_far_away.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Siren_blaring_far_away.wav")))

TTA(text="Siren stops abruptly", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Siren_stops_abruptly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Siren_stops_abruptly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Siren_blaring_far_away.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Siren_stops_abruptly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Crowd murmuring", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crowd_murmuring.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crowd_murmuring.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2ymiXjImwGs.wav"))
