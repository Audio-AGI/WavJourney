
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yoklu5ZJD_2U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A bird chirping intermittently", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_bird_chirping_intermittently.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_bird_chirping_intermittently.wav")))

TTA(text="A bird singing melodiously", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_bird_singing_melodiously.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_bird_singing_melodiously.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_bird_chirping_intermittently.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_bird_singing_melodiously.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Slight plastic crackling noise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Slight_plastic_crackling_noise.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Slight_plastic_crackling_noise.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yoklu5ZJD_2U.wav"))
