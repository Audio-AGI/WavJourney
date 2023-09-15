
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YfK4QBQZ6i7w/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of multiple people laughing", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_multiple_people_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_multiple_people_laughing.wav")))

TTA(text="Laughing sound continues with different laugh types", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughing_sound_continues_with_different.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughing_sound_continues_with_different.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_multiple_people_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughing_sound_continues_with_different.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YfK4QBQZ6i7w.wav"))
