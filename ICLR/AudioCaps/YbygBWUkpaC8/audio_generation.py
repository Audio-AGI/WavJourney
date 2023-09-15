
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YbygBWUkpaC8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is an experience like no other. Feel the wind, hear the birds. Breathe in nature.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_an_experience_like.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_an_experience_like.wav")))

TTA(text="Silence indicating a pause for taking in the environment", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Silence_indicating_a_pause_for.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Silence_indicating_a_pause_for.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_an_experience_like.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Silence_indicating_a_pause_for.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of wind blowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Birds chirping, portraying a peaceful morning", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Birds_chirping_portraying_a_peaceful.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_wind_blowing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Birds_chirping_portraying_a_peaceful.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YbygBWUkpaC8.wav"))
