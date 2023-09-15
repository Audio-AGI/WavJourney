
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_GI7meqlYZk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Cat meowing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Cat_meowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Cat_meowing.wav")))

TTS(text="Oh, you must be hungry. Let me get you some food.", speaker_id="Female2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Oh_you_must_be_hungry.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Oh_you_must_be_hungry.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Cat_meowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Oh_you_must_be_hungry.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_GI7meqlYZk.wav"))
