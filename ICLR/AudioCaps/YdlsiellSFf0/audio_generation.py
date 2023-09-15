
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YdlsiellSFf0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Motorboat engine starts, low rumble", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Motorboat_engine_starts_low_rumble.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Motorboat_engine_starts_low_rumble.wav")))

TTA(text="Motorboat engine revs and increases in volume", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Motorboat_engine_revs_and_increases.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Motorboat_engine_revs_and_increases.wav")))

TTA(text="Motorboat engine screams at full throttle", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Motorboat_engine_screams_at_full.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Motorboat_engine_screams_at_full.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Motorboat_engine_starts_low_rumble.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Motorboat_engine_revs_and_increases.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Motorboat_engine_screams_at_full.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YdlsiellSFf0.wav"))
