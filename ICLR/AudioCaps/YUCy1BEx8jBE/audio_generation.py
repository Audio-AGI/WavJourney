
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YUCy1BEx8jBE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="The tranquility of nature is a balm for the soul. As the water splashes and the music plays, everything else is forgotten.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_The_tranquility_of_nature_is.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_tranquility_of_nature_is.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_tranquility_of_nature_is.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Soothing flute music, lightly playing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Soothing_flute_music_lightly_playing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Gentle splashing of a stream flowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Gentle_splashing_of_a_stream.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Soothing_flute_music_lightly_playing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Gentle_splashing_of_a_stream.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YUCy1BEx8jBE.wav"))
