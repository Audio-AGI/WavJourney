
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YlX3k5p2I_g0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Talks about his excursion plans", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Talks_about_his_excursion_plans.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Talks_about_his_excursion_plans.wav")))

TTS(text="Replies with his suggestion for the trip", speaker_id="Male2_En", volume=-18, out_wav=os.path.join(wav_path, "fg_speech_1_Replies_with_his_suggestion_for.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Replies_with_his_suggestion_for.wav")))

TTA(text="Aircraft engine whines loudly during start up", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Aircraft_engine_whines_loudly_during.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Aircraft_engine_whines_loudly_during.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Talks_about_his_excursion_plans.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Replies_with_his_suggestion_for.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Aircraft_engine_whines_loudly_during.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Distance aircraft engine sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distance_aircraft_engine_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Increasing pitch of aircraft engine as it starts", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Increasing_pitch_of_aircraft_engine.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distance_aircraft_engine_sound.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Increasing_pitch_of_aircraft_engine.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YlX3k5p2I_g0.wav"))
