
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ya0yXS7PmVR0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Heavy rain dying down", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Heavy_rain_dying_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Heavy_rain_dying_down.wav")))

TTA(text="Pause, only light rain can be heard", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Pause_only_light_rain_can.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Pause_only_light_rain_can.wav")))

TTA(text="Heavy rain starting again", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Heavy_rain_starting_again.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Heavy_rain_starting_again.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Heavy_rain_dying_down.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Pause_only_light_rain_can.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Heavy_rain_starting_again.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous rain", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_rain.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_rain.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ya0yXS7PmVR0.wav"))
