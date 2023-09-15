
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9MgGaTbmc6g/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Engine revving up", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Engine_revving_up.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Engine_revving_up.wav")))

TTA(text="Vehicle accelerating", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Vehicle_accelerating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_accelerating.wav")))

TTA(text="Tires skidding on pavement", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Tires_skidding_on_pavement.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Tires_skidding_on_pavement.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Engine_revving_up.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_accelerating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Tires_skidding_on_pavement.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9MgGaTbmc6g.wav"))
