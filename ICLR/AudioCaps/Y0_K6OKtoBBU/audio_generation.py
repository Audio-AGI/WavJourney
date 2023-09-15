
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y0_K6OKtoBBU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rustling sound of leaves", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rustling_sound_of_leaves.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rustling_sound_of_leaves.wav")))

TTA(text="Complete silence", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Complete_silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Complete_silence.wav")))

TTA(text="Cat meowing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Cat_meowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Cat_meowing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rustling_sound_of_leaves.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Complete_silence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Cat_meowing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Distant traffic passing noise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_traffic_passing_noise.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_traffic_passing_noise.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y0_K6OKtoBBU.wav"))
