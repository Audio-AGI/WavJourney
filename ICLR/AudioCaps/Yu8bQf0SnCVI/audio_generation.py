
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yu8bQf0SnCVI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Tapping sound, a rhythmic repeating sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Tapping_sound_a_rhythmic_repeating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Tapping_sound_a_rhythmic_repeating.wav")))

TTA(text="Water spraying sound, high-pressure", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Water_spraying_sound_highpressure.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Water_spraying_sound_highpressure.wav")))

TTA(text="Tapping sound resumes, a rhythmic repeating sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Tapping_sound_resumes_a_rhythmic.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Tapping_sound_resumes_a_rhythmic.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Tapping_sound_a_rhythmic_repeating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Water_spraying_sound_highpressure.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Tapping_sound_resumes_a_rhythmic.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yu8bQf0SnCVI.wav"))
