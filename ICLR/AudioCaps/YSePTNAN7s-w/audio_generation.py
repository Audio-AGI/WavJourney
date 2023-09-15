
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YSePTNAN7s-w/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Excuse me, I will be right back", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Excuse_me_I_will_be.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Excuse_me_I_will_be.wav")))

TTA(text="Toilet flushing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Toilet_flushing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Toilet_flushing.wav")))

TTS(text="Did she just leave during the meeting?", speaker_id="Female2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Did_she_just_leave_during.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Did_she_just_leave_during.wav")))

TTS(text="Looks like it, quite rude actually", speaker_id="News_Female_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Looks_like_it_quite_rude.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Looks_like_it_quite_rude.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Excuse_me_I_will_be.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Toilet_flushing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Did_she_just_leave_during.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Looks_like_it_quite_rude.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:4])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Distant chatter of multiple females", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_chatter_of_multiple_females.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_chatter_of_multiple_females.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YSePTNAN7s-w.wav"))
