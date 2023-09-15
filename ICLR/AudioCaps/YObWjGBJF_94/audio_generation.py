
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YObWjGBJF_94/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="Music playing through a television speaker", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_music_0_Music_playing_through_a_television.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Music_playing_through_a_television.wav")))

TTA(text="Series of plastic clicking sounds", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Series_of_plastic_clicking_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Series_of_plastic_clicking_sounds.wav")))

TTA(text="Continuation of series of plastic clicking sounds", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_series_of_plastic.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_series_of_plastic.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Music_playing_through_a_television.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Series_of_plastic_clicking_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_series_of_plastic.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="White noise hissing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_White_noise_hissing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_White_noise_hissing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YObWjGBJF_94.wav"))
