
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YL8dA-2Lu2hY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="First loud wolf whistle", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_loud_wolf_whistle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_loud_wolf_whistle.wav")))

TTA(text="Silence", length=6, volume=-35, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Silence.wav")))

TTA(text="Second loud wolf whistle", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Second_loud_wolf_whistle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Second_loud_wolf_whistle.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_loud_wolf_whistle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Silence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Second_loud_wolf_whistle.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YL8dA-2Lu2hY.wav"))
