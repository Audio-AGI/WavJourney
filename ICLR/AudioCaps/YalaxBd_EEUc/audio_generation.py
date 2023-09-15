
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YalaxBd_EEUc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Alright, let me show you something amusing.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Alright_let_me_show_you.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Alright_let_me_show_you.wav")))

TTA(text="Series of belches", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Series_of_belches.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Series_of_belches.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Alright_let_me_show_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Series_of_belches.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YalaxBd_EEUc.wav"))
