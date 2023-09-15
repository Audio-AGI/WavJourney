
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPRUfwpmYwJ8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Listen carefully, what I am about to say is vital.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Listen_carefully_what_I_am.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Listen_carefully_what_I_am.wav")))

TTA(text="First burst of intense high-pressure hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_burst_of_intense_highpressure.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_burst_of_intense_highpressure.wav")))

TTA(text="Second burst of intense high-pressure hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_burst_of_intense_highpressure.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_burst_of_intense_highpressure.wav")))

TTA(text="Third burst of intense high-pressure hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Third_burst_of_intense_highpressure.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Third_burst_of_intense_highpressure.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Listen_carefully_what_I_am.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_burst_of_intense_highpressure.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_burst_of_intense_highpressure.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Third_burst_of_intense_highpressure.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPRUfwpmYwJ8.wav"))
