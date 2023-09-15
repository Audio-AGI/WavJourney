
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YXz56Q2Q5j5c/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Metallic rubbing sound, like parts grinding together", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Metallic_rubbing_sound_like_parts.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Metallic_rubbing_sound_like_parts.wav")))

TTS(text="But, while the motor runs, an unusual rubbing occurs", speaker_id="News_Male_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_But_while_the_motor_runs.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_But_while_the_motor_runs.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Metallic_rubbing_sound_like_parts.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_But_while_the_motor_runs.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous low volume electric motor running", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_low_volume_electric_motor.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_low_volume_electric_motor.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YXz56Q2Q5j5c.wav"))
