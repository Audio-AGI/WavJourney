
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9z2OwpftxUE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Distant thundering sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Distant_thundering_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Distant_thundering_sound.wav")))

TTA(text="Another thundering sound closer", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Another_thundering_sound_closer.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Another_thundering_sound_closer.wav")))

TTA(text="Another thundering sound far away", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Another_thundering_sound_far_away.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Another_thundering_sound_far_away.wav")))

TTA(text="Lightning crackling sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Lightning_crackling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Lightning_crackling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Distant_thundering_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Another_thundering_sound_closer.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Another_thundering_sound_far_away.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Lightning_crackling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous soft rain", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_soft_rain.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_soft_rain.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9z2OwpftxUE.wav"))
