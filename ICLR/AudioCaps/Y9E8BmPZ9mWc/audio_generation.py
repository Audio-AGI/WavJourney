
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9E8BmPZ9mWc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Do you hear that sound?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Do_you_hear_that_sound.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Do_you_hear_that_sound.wav")))

TTS(text="Yeah, the engines are roaring today.", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Yeah_the_engines_are_roaring.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yeah_the_engines_are_roaring.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Do_you_hear_that_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yeah_the_engines_are_roaring.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Humming of loud engines", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Humming_of_loud_engines.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Humming_of_loud_engines.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9E8BmPZ9mWc.wav"))
