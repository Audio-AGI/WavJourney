
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YQvATUKXYFBs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Church bells ringing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Church_bells_ringing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Church_bells_ringing.wav")))

TTM(text="Humming of a train approaching from the distance", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_music_0_Humming_of_a_train_approaching.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Humming_of_a_train_approaching.wav")))

TTA(text="Train horn blowing", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Train_horn_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Train_horn_blowing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Church_bells_ringing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Humming_of_a_train_approaching.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Train_horn_blowing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Slight vibrations simulating movement", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Slight_vibrations_simulating_movement.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Slight_vibrations_simulating_movement.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YQvATUKXYFBs.wav"))
