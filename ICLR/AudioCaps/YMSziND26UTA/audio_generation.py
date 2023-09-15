
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMSziND26UTA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Bees buzzing closer", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Bees_buzzing_closer.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Bees_buzzing_closer.wav")))

TTA(text="Multiple dogs howling in the distance", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Multiple_dogs_howling_in_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Multiple_dogs_howling_in_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Bees_buzzing_closer.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Multiple_dogs_howling_in_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Buzzing bees", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Buzzing_bees.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Man singing softly", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Man_singing_softly.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Buzzing_bees.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Man_singing_softly.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMSziND26UTA.wav"))
