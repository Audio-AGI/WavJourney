
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YmaVYiednkSg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rumbling sound approaching", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rumbling_sound_approaching.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rumbling_sound_approaching.wav")))

TTA(text="Spray of liquid", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Spray_of_liquid.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Spray_of_liquid.wav")))

TTS(text="Woah, that was close!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Woah_that_was_close.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Woah_that_was_close.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rumbling_sound_approaching.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Spray_of_liquid.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Woah_that_was_close.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YmaVYiednkSg.wav"))
