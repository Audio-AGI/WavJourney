
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y3RultJjvTWI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vibration sounds of an object shaking", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vibration_sounds_of_an_object.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vibration_sounds_of_an_object.wav")))

TTA(text="Splashing water sounds", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Splashing_water_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Splashing_water_sounds.wav")))

TTS(text="What was that?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_What_was_that.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_was_that.wav")))

TTS(text="I'm not sure. Let's check it out.", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Im_not_sure_Lets_check.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Im_not_sure_Lets_check.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vibration_sounds_of_an_object.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Splashing_water_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_was_that.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Im_not_sure_Lets_check.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y3RultJjvTWI.wav"))
