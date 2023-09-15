
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YoiIi6H83Y38/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Motorcycle engine starting up", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Motorcycle_engine_starting_up.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Motorcycle_engine_starting_up.wav")))

TTA(text="Motorcycle engine revving several times", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Motorcycle_engine_revving_several_times.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Motorcycle_engine_revving_several_times.wav")))

TTS(text="Random conversations about ordinary daily life", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Random_conversations_about_ordinary_daily.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Random_conversations_about_ordinary_daily.wav")))

TTA(text="Motorcycle engine shutting down", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Motorcycle_engine_shutting_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Motorcycle_engine_shutting_down.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Motorcycle_engine_starting_up.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Motorcycle_engine_revving_several_times.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Random_conversations_about_ordinary_daily.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Motorcycle_engine_shutting_down.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Wind blows into a microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Wind_blows_into_a_microphone.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Wind_blows_into_a_microphone.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YoiIi6H83Y38.wav"))
