
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9ZZHvwaH-CU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_6_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_6_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_7_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_7_Single_gunshot.wav")))

TTA(text="Single gunshot", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_8_Single_gunshot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_8_Single_gunshot.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_6_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_7_Single_gunshot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_8_Single_gunshot.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:9])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Gunfire noise, repetitive and constant", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Gunfire_noise_repetitive_and_constant.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:9])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="People screaming in panic", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_People_screaming_in_panic.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Gunfire_noise_repetitive_and_constant.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_People_screaming_in_panic.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9ZZHvwaH-CU.wav"))
