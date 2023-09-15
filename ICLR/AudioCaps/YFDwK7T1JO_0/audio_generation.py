
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFDwK7T1JO_0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Did you double-check the measurements?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Did_you_doublecheck_the_measurements.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Did_you_doublecheck_the_measurements.wav")))

TTS(text="Yes, everything is perfectly aligned.", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_everything_is_perfectly_aligned.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_everything_is_perfectly_aligned.wav")))

TTA(text="Sound of plastic clacking", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_plastic_clacking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_plastic_clacking.wav")))

TTA(text="Power tool drilling sound", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Power_tool_drilling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Power_tool_drilling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Did_you_doublecheck_the_measurements.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_everything_is_perfectly_aligned.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_plastic_clacking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Power_tool_drilling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFDwK7T1JO_0.wav"))
