
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YrvtA7c1I4xo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Swoosh sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Swoosh_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Swoosh_sound.wav")))

TTS(text="And, that's how you do it.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_And_thats_how_you_do.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_And_thats_how_you_do.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Swoosh_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_And_thats_how_you_do.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Shoes squeaking on the floor", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Shoes_squeaking_on_the_floor.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Shoes_squeaking_on_the_floor.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YrvtA7c1I4xo.wav"))
