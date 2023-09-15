
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YSZ6CcXINiiE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is the best thing you will ever hear! Wait for it...", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_the_best_thing.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_the_best_thing.wav")))

TTA(text="A loud bursting sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_loud_bursting_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_loud_bursting_sound.wav")))

TTA(text="People laughing with joy and amusement", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_People_laughing_with_joy_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_People_laughing_with_joy_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_the_best_thing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_loud_bursting_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_People_laughing_with_joy_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YSZ6CcXINiiE.wav"))
