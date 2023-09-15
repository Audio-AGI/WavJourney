
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtfOIhQpYYe8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Seems like a helicopter is passing right now. I can see it flying away...", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Seems_like_a_helicopter_is.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Seems_like_a_helicopter_is.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Seems_like_a_helicopter_is.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of a helicopter flying by", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_helicopter_flying.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_helicopter_flying.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtfOIhQpYYe8.wav"))
