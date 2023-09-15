
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YI_8KqxP5xOA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Light hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Light_hissing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Light_hissing.wav")))

TTA(text="Pause", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Pause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Pause.wav")))

TTA(text="Light hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Light_hissing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Light_hissing.wav")))

TTA(text="Pause", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Pause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Pause.wav")))

TTA(text="Light hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Light_hissing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Light_hissing.wav")))

TTA(text="Pause", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Pause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Pause.wav")))

TTA(text="Light hissing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_6_Light_hissing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_6_Light_hissing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Light_hissing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Pause.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Light_hissing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Pause.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Light_hissing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Pause.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_6_Light_hissing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YI_8KqxP5xOA.wav"))
