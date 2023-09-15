
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YrPkCYq4Zjwk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Synthesized rumble", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Synthesized_rumble.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Synthesized_rumble.wav")))

TTS(text="This is a robotic woman speaking", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_a_robotic_woman.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_a_robotic_woman.wav")))

TTA(text="Electronic beeps", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Electronic_beeps.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beeps.wav")))

TTS(text="Now, a human is speaking", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Now_a_human_is_speaking.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Now_a_human_is_speaking.wav")))

TTS(text="This is intercom speaking while music plays", speaker_id="News_Male_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_This_is_intercom_speaking_while.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_This_is_intercom_speaking_while.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Synthesized_rumble.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_a_robotic_woman.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beeps.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Now_a_human_is_speaking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_This_is_intercom_speaking_while.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[4:5])
bg_audio_offset = sum(fg_audio_lens[:4])
TTM(text="Soft ambient music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Soft_ambient_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Soft_ambient_music.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YrPkCYq4Zjwk.wav"))
