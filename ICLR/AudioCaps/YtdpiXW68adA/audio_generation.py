
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtdpiXW68adA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sobbing sound of a woman", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sobbing_sound_of_a_woman.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sobbing_sound_of_a_woman.wav")))

TTS(text="Please, don't cry. Everything will be alright", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Please_dont_cry_Everything_will.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Please_dont_cry_Everything_will.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sobbing_sound_of_a_woman.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Please_dont_cry_Everything_will.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtdpiXW68adA.wav"))
