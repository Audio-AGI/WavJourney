
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2sZhC_mKeic/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Soft cat meow", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Soft_cat_meow.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Soft_cat_meow.wav")))

TTA(text="Thud of a book hitting the ground", length=8, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Thud_of_a_book_hitting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Thud_of_a_book_hitting.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Soft_cat_meow.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Thud_of_a_book_hitting.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Distant muffled ambient noises, very low intensity", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_muffled_ambient_noises_very.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_muffled_ambient_noises_very.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2sZhC_mKeic.wav"))
