
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YsJrFyjfrL-g/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sharp metal clack", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sharp_metal_clack.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sharp_metal_clack.wav")))

TTA(text="Another sharp metal clack", length=2, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Another_sharp_metal_clack.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Another_sharp_metal_clack.wav")))

TTA(text="Yet another sharp metal clack", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Yet_another_sharp_metal_clack.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Yet_another_sharp_metal_clack.wav")))

TTA(text="Final sharp metal clack", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Final_sharp_metal_clack.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Final_sharp_metal_clack.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sharp_metal_clack.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Another_sharp_metal_clack.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Yet_another_sharp_metal_clack.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Final_sharp_metal_clack.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous sound of a working sewing machine", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_sound_of_a_working.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_sound_of_a_working.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YsJrFyjfrL-g.wav"))
