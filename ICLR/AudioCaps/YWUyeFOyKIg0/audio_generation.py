
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YWUyeFOyKIg0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Let's get ready for the race", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Lets_get_ready_for_the.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Lets_get_ready_for_the.wav")))

TTA(text="Distant horn blowing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Distant_horn_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Distant_horn_blowing.wav")))

TTA(text="Race car engine revving and speeding away", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Race_car_engine_revving_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Race_car_engine_revving_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Lets_get_ready_for_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Distant_horn_blowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Race_car_engine_revving_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Ambient sound of a bustling crowd", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Ambient_sound_of_a_bustling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Ambient_sound_of_a_bustling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YWUyeFOyKIg0.wav"))
