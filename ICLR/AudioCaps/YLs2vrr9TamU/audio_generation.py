
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YLs2vrr9TamU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Monotonous humming from a motor", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Monotonous_humming_from_a_motor.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Monotonous_humming_from_a_motor.wav")))

TTA(text="Loud dry cracking sound", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_dry_cracking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_dry_cracking_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Monotonous_humming_from_a_motor.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_dry_cracking_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YLs2vrr9TamU.wav"))
