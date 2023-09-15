
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpI_kPedctoo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Motorcycle engine started with a roar", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Motorcycle_engine_started_with_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Motorcycle_engine_started_with_a.wav")))

TTA(text="Motorcycle engine running at high revs", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Motorcycle_engine_running_at_high.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Motorcycle_engine_running_at_high.wav")))

TTA(text="Motorcycle engine stopped abruptly", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Motorcycle_engine_stopped_abruptly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Motorcycle_engine_stopped_abruptly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Motorcycle_engine_started_with_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Motorcycle_engine_running_at_high.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Motorcycle_engine_stopped_abruptly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpI_kPedctoo.wav"))
