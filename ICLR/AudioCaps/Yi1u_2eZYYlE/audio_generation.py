
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yi1u_2eZYYlE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A short buzzer sound creating vibration", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_short_buzzer_sound_creating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_short_buzzer_sound_creating.wav")))

TTA(text="A short pause with no sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_short_pause_with_no.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_short_pause_with_no.wav")))

TTA(text="A short buzzer sound creating vibration", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_A_short_buzzer_sound_creating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_A_short_buzzer_sound_creating.wav")))

TTA(text="A short pause with no sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_A_short_pause_with_no.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_A_short_pause_with_no.wav")))

TTA(text="A short buzzer sound creating vibration", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_A_short_buzzer_sound_creating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_A_short_buzzer_sound_creating.wav")))

TTA(text="A short pause with no sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_5_A_short_pause_with_no.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_A_short_pause_with_no.wav")))

TTA(text="A short buzzer sound creating vibration", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_6_A_short_buzzer_sound_creating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_6_A_short_buzzer_sound_creating.wav")))

TTA(text="A short pause with no sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_7_A_short_pause_with_no.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_7_A_short_pause_with_no.wav")))

TTA(text="A short buzzer sound creating vibration", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_8_A_short_buzzer_sound_creating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_8_A_short_buzzer_sound_creating.wav")))

TTA(text="A short pause with no sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_9_A_short_pause_with_no.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_9_A_short_pause_with_no.wav")))

TTA(text="A short buzzer sound creating vibration", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_10_A_short_buzzer_sound_creating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_10_A_short_buzzer_sound_creating.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_short_buzzer_sound_creating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_short_pause_with_no.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_A_short_buzzer_sound_creating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_A_short_pause_with_no.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_A_short_buzzer_sound_creating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_A_short_pause_with_no.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_6_A_short_buzzer_sound_creating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_7_A_short_pause_with_no.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_8_A_short_buzzer_sound_creating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_9_A_short_pause_with_no.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_10_A_short_buzzer_sound_creating.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yi1u_2eZYYlE.wav"))
