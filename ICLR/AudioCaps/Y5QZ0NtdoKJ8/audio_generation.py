
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y5QZ0NtdoKJ8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Digital beeping sound repeating for 6 seconds", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Digital_beeping_sound_repeating_for.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Digital_beeping_sound_repeating_for.wav")))

TTS(text="We apologize for the inconvenience, but our systems are currently experiencing technical difficulties.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_We_apologize_for_the_inconvenience.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_We_apologize_for_the_inconvenience.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Digital_beeping_sound_repeating_for.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_We_apologize_for_the_inconvenience.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y5QZ0NtdoKJ8.wav"))
