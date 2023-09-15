
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YwFiCblfZ-vg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Static noise", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Static_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Static_noise.wav")))

TTS(text="This is a test of the Emergency Broadcast System. This is only a test.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_a_test_of.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_a_test_of.wav")))

TTA(text="Static noise", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Static_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Static_noise.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Static_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_a_test_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Static_noise.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YwFiCblfZ-vg.wav"))
