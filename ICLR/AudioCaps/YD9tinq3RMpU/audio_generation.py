
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YD9tinq3RMpU/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This new technology with its immense potential can revolutionize our world.", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_new_technology_with_its.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_new_technology_with_its.wav")))

TTS(text="We need to take precautionary steps to ensure safety.", speaker_id="News_Female_En", volume=-18, out_wav=os.path.join(wav_path, "fg_speech_1_We_need_to_take_precautionary.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_We_need_to_take_precautionary.wav")))

TTS(text="Aligned with the country's development goals, this agenda is a priority.", speaker_id="Male1_En", volume=-19, out_wav=os.path.join(wav_path, "fg_speech_2_Aligned_with_the_countrys_development.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Aligned_with_the_countrys_development.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_new_technology_with_its.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_We_need_to_take_precautionary.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Aligned_with_the_countrys_development.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Engine running sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Engine_running_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Engine_running_sound.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YD9tinq3RMpU.wav"))
