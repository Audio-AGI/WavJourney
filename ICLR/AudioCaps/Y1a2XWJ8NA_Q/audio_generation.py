
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1a2XWJ8NA_Q/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="So, here's the thing about engines...", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_So_heres_the_thing_about.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_So_heres_the_thing_about.wav")))

TTS(text="Mhm, I'm listening...", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Mhm_Im_listening.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Mhm_Im_listening.wav")))

TTS(text="They're more than just moving parts. They're like a symphony.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Theyre_more_than_just_moving.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Theyre_more_than_just_moving.wav")))

TTS(text="Sounds fascinating. Tell me more.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_3_Sounds_fascinating_Tell_me_more.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_Sounds_fascinating_Tell_me_more.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_So_heres_the_thing_about.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Mhm_Im_listening.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Theyre_more_than_just_moving.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_Sounds_fascinating_Tell_me_more.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Engine running, with occasional clicks and sputters", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Engine_running_with_occasional_clicks.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="The sound of wind blowing gently", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_The_sound_of_wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Engine_running_with_occasional_clicks.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_The_sound_of_wind_blowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1a2XWJ8NA_Q.wav"))
