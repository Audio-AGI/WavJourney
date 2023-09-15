
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YlHh0SwUhP8U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Gunshot sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Gunshot_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Gunshot_sound.wav")))

TTA(text="Click and clack sound", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Click_and_clack_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Click_and_clack_sound.wav")))

TTA(text="Second gunshot sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Second_gunshot_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Second_gunshot_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Gunshot_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Click_and_clack_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Second_gunshot_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YlHh0SwUhP8U.wav"))
