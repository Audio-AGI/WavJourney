
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yup2PpjTzyyc/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="Happy introductory piano music", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_music_0_Happy_introductory_piano_music.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Happy_introductory_piano_music.wav")))

TTS(text="Hello, welcome to the show.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_welcome_to_the_show.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_welcome_to_the_show.wav")))

TTA(text="Short beep sequence", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Short_beep_sequence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Short_beep_sequence.wav")))

TTM(text="Person singing a joyful tune", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_music_1_Person_singing_a_joyful_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_1_Person_singing_a_joyful_tune.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Happy_introductory_piano_music.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_welcome_to_the_show.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Short_beep_sequence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_1_Person_singing_a_joyful_tune.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yup2PpjTzyyc.wav"))
