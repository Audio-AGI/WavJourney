
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtxeXrpoMST4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of someone approaching", length=8, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_someone_approaching.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_someone_approaching.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_someone_approaching.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Water running in background, slowly getting louder", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Water_running_in_background_slowly.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Water_running_in_background_slowly.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtxeXrpoMST4.wav"))
