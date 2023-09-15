
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YKel-hfZ_9h8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of rustling leaves", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_rustling_leaves.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_rustling_leaves.wav")))

TTS(text="What a lovely day it is, isn't it?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_lovely_day_it.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_lovely_day_it.wav")))

TTA(text="Child's laughter", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Childs_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Childs_laughter.wav")))

TTA(text="Sound of rustling leaves fading away", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_rustling_leaves_fading.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_rustling_leaves_fading.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_rustling_leaves.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_lovely_day_it.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Childs_laughter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_rustling_leaves_fading.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YKel-hfZ_9h8.wav"))
