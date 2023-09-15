
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y5xC4hkAWiao/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Car engine running", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Car_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_running.wav")))

TTA(text="Loud stuttering noise", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_stuttering_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_stuttering_noise.wav")))

TTA(text="Pause", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Pause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Pause.wav")))

TTA(text="Loud stuttering noise", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Loud_stuttering_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Loud_stuttering_noise.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_stuttering_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Pause.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Loud_stuttering_noise.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y5xC4hkAWiao.wav"))
