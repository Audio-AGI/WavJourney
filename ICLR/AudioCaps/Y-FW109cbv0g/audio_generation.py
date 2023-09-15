
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-FW109cbv0g/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Speech followed by quietness", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Speech_followed_by_quietness.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Speech_followed_by_quietness.wav")))

TTA(text="Silence", length=3, volume=-30, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Silence.wav")))

TTS(text="and a man speaks", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_and_a_man_speaks.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_and_a_man_speaks.wav")))

TTA(text="Laughter of a man", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_man.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_man.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Speech_followed_by_quietness.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Silence.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_and_a_man_speaks.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_man.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-FW109cbv0g.wav"))
