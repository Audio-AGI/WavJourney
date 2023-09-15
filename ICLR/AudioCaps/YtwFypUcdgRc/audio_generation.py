
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YtwFypUcdgRc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="A breezy day with conversations filling the air as machinery hums along in the background.", speaker_id="News_Male_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_A_breezy_day_with_conversations.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_A_breezy_day_with_conversations.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_A_breezy_day_with_conversations.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing gently", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing_gently.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="People speaking indistinctly in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_People_speaking_indistinctly_in_the.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Distant humming of machinery", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Distant_humming_of_machinery.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Wind_blowing_gently.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_People_speaking_indistinctly_in_the.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Distant_humming_of_machinery.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YtwFypUcdgRc.wav"))
