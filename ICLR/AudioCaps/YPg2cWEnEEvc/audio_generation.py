
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPg2cWEnEEvc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Long burping sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Long_burping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Long_burping_sound.wav")))

TTA(text="Short follow-up burping sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Short_followup_burping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Short_followup_burping_sound.wav")))

TTA(text="Loud farting sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Loud_farting_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Loud_farting_sound.wav")))

TTA(text="Silent but deadly farting sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Silent_but_deadly_farting_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Silent_but_deadly_farting_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Long_burping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Short_followup_burping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Loud_farting_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Silent_but_deadly_farting_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPg2cWEnEEvc.wav"))
