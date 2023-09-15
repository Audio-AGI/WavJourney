
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPMMdAKZxI_I/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud burping sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_burping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_burping_sound.wav")))

TTA(text="Women laughing", length=2, volume=-22, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Women_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Women_laughing.wav")))

TTS(text="While these events were happening, there was a lively discussion in the background.", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_While_these_events_were_happening.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_While_these_events_were_happening.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_burping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Women_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_While_these_events_were_happening.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Man talking in background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Man_talking_in_background.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Woman talking in background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Woman_talking_in_background.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Man_talking_in_background.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Woman_talking_in_background.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPMMdAKZxI_I.wav"))
