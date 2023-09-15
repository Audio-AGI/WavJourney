
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YXQxIXaX_7M0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of water running, more upfront", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_water_running_more.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_water_running_more.wav")))

TTA(text="Distant indistinct speech, slightly clearer", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Distant_indistinct_speech_slightly_clearer.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Distant_indistinct_speech_slightly_clearer.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_water_running_more.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Distant_indistinct_speech_slightly_clearer.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of water running", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_running.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Distant indistinct speech", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Distant_indistinct_speech.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_running.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Distant_indistinct_speech.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YXQxIXaX_7M0.wav"))
