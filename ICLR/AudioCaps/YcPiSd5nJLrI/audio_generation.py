
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YcPiSd5nJLrI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud bangs", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_bangs.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_bangs.wav")))

TTA(text="Slow motion rumble", length=6, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Slow_motion_rumble.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Slow_motion_rumble.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_bangs.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Slow_motion_rumble.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="People speaking, lively chatter", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_People_speaking_lively_chatter.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_People_speaking_lively_chatter.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YcPiSd5nJLrI.wav"))
