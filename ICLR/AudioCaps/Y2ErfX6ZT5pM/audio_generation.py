
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2ErfX6ZT5pM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Mum, where are you?", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Mum_where_are_you.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Mum_where_are_you.wav")))

TTA(text="Distant toilet flushing sound", length=7, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Distant_toilet_flushing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Distant_toilet_flushing_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Mum_where_are_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Distant_toilet_flushing_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2ErfX6ZT5pM.wav"))
