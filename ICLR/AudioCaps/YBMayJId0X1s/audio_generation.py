
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBMayJId0X1s/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, can anyone hear me? I need assistance here!", speaker_id="Male1_En", volume=-22, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_can_anyone_hear_me.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_can_anyone_hear_me.wav")))

TTA(text="Brief break in the radio transmission", length=1, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Brief_break_in_the_radio.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Brief_break_in_the_radio.wav")))

TTA(text="Crying baby sound", length=4, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Crying_baby_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Crying_baby_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_can_anyone_hear_me.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Brief_break_in_the_radio.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Crying_baby_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Static radio sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Static_radio_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Static_radio_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBMayJId0X1s.wav"))
