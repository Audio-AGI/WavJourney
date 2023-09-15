
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YQRtuOWWya30/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Splashing water sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Splashing_water_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Splashing_water_sound.wav")))

TTA(text="Rustling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Rustling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Rustling_sound.wav")))

TTS(text="In spite of all previous signs, we have successfully managed to manoeuvre our way through this challenging situation", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_In_spite_of_all_previous.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_In_spite_of_all_previous.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Splashing_water_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Rustling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_In_spite_of_all_previous.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YQRtuOWWya30.wav"))
