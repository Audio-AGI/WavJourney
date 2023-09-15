
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ye9MWXS34o48/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Woman breathing heavily", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Woman_breathing_heavily.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Woman_breathing_heavily.wav")))

TTA(text="Two sneezes in succession", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Two_sneezes_in_succession.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Two_sneezes_in_succession.wav")))

TTA(text="Nose sniffling sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Nose_sniffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Nose_sniffling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Woman_breathing_heavily.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Two_sneezes_in_succession.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Nose_sniffling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ye9MWXS34o48.wav"))
