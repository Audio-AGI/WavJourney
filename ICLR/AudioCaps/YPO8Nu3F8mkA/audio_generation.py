
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPO8Nu3F8mkA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Gunshot firing in the distance", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Gunshot_firing_in_the_distance.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Gunshot_firing_in_the_distance.wav")))

TTA(text="Steam hissing", length=8, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Steam_hissing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Steam_hissing.wav")))

TTA(text="Fire crackling", length=8, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Fire_crackling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Fire_crackling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Gunshot_firing_in_the_distance.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Steam_hissing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Fire_crackling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPO8Nu3F8mkA.wav"))
