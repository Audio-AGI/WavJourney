
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YTaQKhIRwii4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A continuous crowd applause mixed with a muffled speaker", length=10, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_continuous_crowd_applause_mixed.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_continuous_crowd_applause_mixed.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_continuous_crowd_applause_mixed.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of crowd applause", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_crowd_applause.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of a muffled speaker", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_a_muffled_speaker.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_crowd_applause.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_a_muffled_speaker.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YTaQKhIRwii4.wav"))
