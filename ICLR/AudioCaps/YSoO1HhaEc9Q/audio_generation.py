
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YSoO1HhaEc9Q/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Mechanical noises", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Mechanical_noises.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Mechanical_noises.wav")))

TTA(text="Pigs oinking", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Pigs_oinking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Pigs_oinking.wav")))

TTS(text="Quite a spectacle, isn't it?", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Quite_a_spectacle_isnt_it.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Quite_a_spectacle_isnt_it.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Mechanical_noises.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Pigs_oinking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Quite_a_spectacle_isnt_it.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YSoO1HhaEc9Q.wav"))
