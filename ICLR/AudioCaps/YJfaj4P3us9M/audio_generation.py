
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YJfaj4P3us9M/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Telephone dialing tone", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Telephone_dialing_tone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Telephone_dialing_tone.wav")))

TTA(text="Plastic switch flipping on", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_switch_flipping_on.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_switch_flipping_on.wav")))

TTA(text="Plastic switch flipping off", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Plastic_switch_flipping_off.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Plastic_switch_flipping_off.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Telephone_dialing_tone.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_switch_flipping_on.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Plastic_switch_flipping_off.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YJfaj4P3us9M.wav"))
