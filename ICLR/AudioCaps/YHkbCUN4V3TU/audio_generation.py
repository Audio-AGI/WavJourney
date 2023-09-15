
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHkbCUN4V3TU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Baby whining sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Baby_whining_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Baby_whining_sound.wav")))

TTA(text="Baby laughing sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Baby_laughing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Baby_laughing_sound.wav")))

TTS(text="Oh aren't you just the cutest! I love your laugh honey.", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Oh_arent_you_just_the.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Oh_arent_you_just_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Baby_whining_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Baby_laughing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Oh_arent_you_just_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHkbCUN4V3TU.wav"))
