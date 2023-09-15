
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YF-47fRplQEc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Isn't this the most serene sight you've ever experienced?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Isnt_this_the_most_serene.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Isnt_this_the_most_serene.wav")))

TTS(text="It absolutely is. I love how peaceful it is here.", speaker_id="Female2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_It_absolutely_is_I_love.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_It_absolutely_is_I_love.wav")))

TTS(text="And those cute little lambs are just the cherry on top.", speaker_id="News_Female_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_2_And_those_cute_little_lambs.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_And_those_cute_little_lambs.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Isnt_this_the_most_serene.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_It_absolutely_is_I_love.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_And_those_cute_little_lambs.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous sheep bleating", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_sheep_bleating.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_sheep_bleating.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YF-47fRplQEc.wav"))
