
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YP12nvSpKXcs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Insect buzzing sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Insect_buzzing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Insect_buzzing_sound.wav")))

TTA(text="Muffled plastic camera sound", length=2, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Muffled_plastic_camera_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Muffled_plastic_camera_sound.wav")))

TTS(text="Look at this awesome bug!", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Look_at_this_awesome_bug.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Look_at_this_awesome_bug.wav")))

TTA(text="Footsteps on foliage sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Footsteps_on_foliage_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Footsteps_on_foliage_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Insect_buzzing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Muffled_plastic_camera_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Look_at_this_awesome_bug.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Footsteps_on_foliage_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuing insect buzz", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuing_insect_buzz.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuing_insect_buzz.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YP12nvSpKXcs.wav"))
