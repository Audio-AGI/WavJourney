
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YDjKGzOe_COc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, my name is Lucy. I am six years old.", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_my_name_is_Lucy.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_my_name_is_Lucy.wav")))

TTA(text="Soft echo", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Soft_echo.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Soft_echo.wav")))

TTA(text="Sound of a quiet room", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_quiet_room.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_quiet_room.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_my_name_is_Lucy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Soft_echo.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_quiet_room.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Soft rustling of paper", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Soft_rustling_of_paper.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Soft_rustling_of_paper.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YDjKGzOe_COc.wav"))
