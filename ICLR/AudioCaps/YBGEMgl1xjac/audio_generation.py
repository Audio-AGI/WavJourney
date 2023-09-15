
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBGEMgl1xjac/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="High-pitched cricket chirping", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Highpitched_cricket_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Highpitched_cricket_chirping.wav")))

TTA(text="Low-pitched bird tweet", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Lowpitched_bird_tweet.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Lowpitched_bird_tweet.wav")))

TTA(text="High-pitched bird twitter", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Highpitched_bird_twitter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Highpitched_bird_twitter.wav")))

TTA(text="Buzz of a bee", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Buzz_of_a_bee.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Buzz_of_a_bee.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Highpitched_cricket_chirping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Lowpitched_bird_tweet.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Highpitched_bird_twitter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Buzz_of_a_bee.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Chirping of various birds", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Chirping_of_various_birds.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Humming of various insects", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Humming_of_various_insects.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Chirping_of_various_birds.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Humming_of_various_insects.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBGEMgl1xjac.wav"))
