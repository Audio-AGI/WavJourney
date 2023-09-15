
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIKnx3hJv1bs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of liquid spraying", length=6, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_liquid_spraying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_liquid_spraying.wav")))

TTA(text="Sound of hissing air", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_hissing_air.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_hissing_air.wav")))

TTA(text="Sound of light vibrations", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_light_vibrations.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_light_vibrations.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_liquid_spraying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_hissing_air.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_light_vibrations.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIKnx3hJv1bs.wav"))
