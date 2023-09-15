
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YlVr-PxhZo8s/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Indistinct sound from microphone", length=10, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Indistinct_sound_from_microphone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Indistinct_sound_from_microphone.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Indistinct_sound_from_microphone.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Idling vehicle engine", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Idling_vehicle_engine.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Idling_vehicle_engine.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YlVr-PxhZo8s.wav"))
