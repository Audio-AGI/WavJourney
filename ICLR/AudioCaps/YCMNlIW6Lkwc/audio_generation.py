
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCMNlIW6Lkwc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Gun shot sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Gun_shot_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Gun_shot_sound.wav")))

TTA(text="Explosion sound", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Explosion_sound.wav")))

TTS(text="Hahaha, that was epic!", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hahaha_that_was_epic.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hahaha_that_was_epic.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Gun_shot_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Explosion_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hahaha_that_was_epic.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCMNlIW6Lkwc.wav"))
