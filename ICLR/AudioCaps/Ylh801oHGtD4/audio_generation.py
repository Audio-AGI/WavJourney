
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ylh801oHGtD4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Small motor buzzing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Small_motor_buzzing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Small_motor_buzzing.wav")))

TTS(text="The job is done. I'll be on my way.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_The_job_is_done_Ill.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_job_is_done_Ill.wav")))

TTA(text="Metal door closing", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_door_closing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_door_closing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Small_motor_buzzing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_job_is_done_Ill.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_door_closing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ylh801oHGtD4.wav"))
