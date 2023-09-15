
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yu84FiZ_omhA/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="A woman singing a smooth melody", length=7, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_A_woman_singing_a_smooth.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_A_woman_singing_a_smooth.wav")))

TTA(text="Choking sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Choking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Choking_sound.wav")))

TTA(text="Birds chirping", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_A_woman_singing_a_smooth.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Choking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yu84FiZ_omhA.wav"))
