
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-mb4Fw4Z0xg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="What a race! These drivers are really pushing their cars to the limit!", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_race_These_drivers.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_race_These_drivers.wav")))

TTA(text="Sound of cars speeding", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_cars_speeding.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_cars_speeding.wav")))

TTS(text="The audience are loving every bit of this action-packed race!", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_The_audience_are_loving_every.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_The_audience_are_loving_every.wav")))

TTS(text="Go number 23! You can do it!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_2_Go_number__You_can.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Go_number__You_can.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_race_These_drivers.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_cars_speeding.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_The_audience_are_loving_every.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Go_number__You_can.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of race cars speeding on a race track", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_race_cars_speeding.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Sound of crowd talking and cheering", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_crowd_talking_and.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_race_cars_speeding.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_crowd_talking_and.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-mb4Fw4Z0xg.wav"))
