
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBzHTqyX69pI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Scraping sound, like branches being dragged across a rough surface", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Scraping_sound_like_branches_being.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Scraping_sound_like_branches_being.wav")))

TTA(text="Continued scraping sound, a bit more intense", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Continued_scraping_sound_a_bit.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Continued_scraping_sound_a_bit.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Scraping_sound_like_branches_being.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Continued_scraping_sound_a_bit.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Rustling sound, possibly leaves or similar materials", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Rustling_sound_possibly_leaves_or.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Pigeons coo softly in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Pigeons_coo_softly_in_the.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Rustling_sound_possibly_leaves_or.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Pigeons_coo_softly_in_the.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBzHTqyX69pI.wav"))
