
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7XUt6sQS7nM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="What a beautiful day, don't you think?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_dont.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_dont.wav")))

TTA(text="Animals bleating", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Animals_bleating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Animals_bleating.wav")))

TTS(text="Yes, it sure is. The weather is just perfect.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_it_sure_is_The.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_it_sure_is_The.wav")))

TTA(text="Animals bleating", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Animals_bleating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Animals_bleating.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_dont.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Animals_bleating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_it_sure_is_The.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Animals_bleating.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Rustling noises, like leaves or paper", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Rustling_noises_like_leaves_or.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Rustling_noises_like_leaves_or.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7XUt6sQS7nM.wav"))
