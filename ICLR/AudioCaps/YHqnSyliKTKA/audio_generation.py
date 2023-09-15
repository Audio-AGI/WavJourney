
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHqnSyliKTKA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I am here at the park, and there's a busy crowd all around me.", speaker_id="News_Female_Out_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_am_here_at_the.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_female_speaker_outside.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_am_here_at_the.wav")))

TTA(text="Horse neighing sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Horse_neighing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Horse_neighing_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_am_here_at_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Horse_neighing_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Crowd of people talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Lawn mower engine running", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Lawn_mower_engine_running.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_talking.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Lawn_mower_engine_running.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHqnSyliKTKA.wav"))
