
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4IeDBwyQ9ZQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, how are you today?", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_how_are_you_today.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_how_are_you_today.wav")))

TTA(text="We hear a rustling sound as if someone is shifting papers", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_We_hear_a_rustling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_We_hear_a_rustling_sound.wav")))

TTS(text="Hi, I'm good. How about you?", speaker_id="Female2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Hi_Im_good_How_about.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hi_Im_good_How_about.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_how_are_you_today.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_We_hear_a_rustling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hi_Im_good_How_about.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4IeDBwyQ9ZQ.wav"))
