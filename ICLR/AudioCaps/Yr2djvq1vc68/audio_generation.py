
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yr2djvq1vc68/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Water pouring out of a faucet at a high rate", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Water_pouring_out_of_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Water_pouring_out_of_a.wav")))

TTA(text="Container filling with liquid", length=3, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Container_filling_with_liquid.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Container_filling_with_liquid.wav")))

TTA(text="Splashing of liquid coming out from the container", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Splashing_of_liquid_coming_out.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Splashing_of_liquid_coming_out.wav")))

TTA(text="Scrubbing sound on a plastic surface", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Scrubbing_sound_on_a_plastic.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Scrubbing_sound_on_a_plastic.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Water_pouring_out_of_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Container_filling_with_liquid.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Splashing_of_liquid_coming_out.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Scrubbing_sound_on_a_plastic.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yr2djvq1vc68.wav"))
