
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YE9zN3-C64KE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="And now for something truly astonishing", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_And_now_for_something_truly.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_And_now_for_something_truly.wav")))

TTA(text="Pig oinking sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Pig_oinking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Pig_oinking_sound.wav")))

TTS(text="Wasn't that just delightful", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Wasnt_that_just_delightful.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Wasnt_that_just_delightful.wav")))

TTA(text="Cloth rustling sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Cloth_rustling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Cloth_rustling_sound.wav")))

TTA(text="Camera muffling sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Camera_muffling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Camera_muffling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_And_now_for_something_truly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Pig_oinking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Wasnt_that_just_delightful.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Cloth_rustling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Camera_muffling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YE9zN3-C64KE.wav"))
