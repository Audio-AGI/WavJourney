
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YWOywdRmySs0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="You know, life is like a box of chocolates.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_You_know_life_is_like.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_You_know_life_is_like.wav")))

TTA(text="Noise of plastic crumpling and crinkling", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Noise_of_plastic_crumpling_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Noise_of_plastic_crumpling_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_You_know_life_is_like.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Noise_of_plastic_crumpling_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YWOywdRmySs0.wav"))
