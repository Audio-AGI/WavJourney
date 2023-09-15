
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHqndxoujCYI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud ringing of a clock", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_ringing_of_a_clock.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_ringing_of_a_clock.wav")))

TTA(text="Faint ticking of a clock, louder than the background ticking sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Faint_ticking_of_a_clock.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Faint_ticking_of_a_clock.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_ringing_of_a_clock.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Faint_ticking_of_a_clock.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Faint ticking of a clock", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Faint_ticking_of_a_clock.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Faint_ticking_of_a_clock.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHqndxoujCYI.wav"))
