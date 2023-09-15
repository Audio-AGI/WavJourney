
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YrjUrB1WUpcI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="The sound of a sink faucet being turned on", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_a_sink.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_a_sink.wav")))

TTA(text="The sound of water pouring from the faucet", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_The_sound_of_water_pouring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_The_sound_of_water_pouring.wav")))

TTA(text="The gurgling sound of water draining down a pipe", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_The_gurgling_sound_of_water.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_The_gurgling_sound_of_water.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_a_sink.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_The_sound_of_water_pouring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_The_gurgling_sound_of_water.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YrjUrB1WUpcI.wav"))
