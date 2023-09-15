
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YA61Mry8zBwE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Different kinds of animals sounds", length=10, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Different_kinds_of_animals_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Different_kinds_of_animals_sounds.wav")))

TTM(text="Drum roll", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Drum_roll.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Drum_roll.wav")))

TTA(text="Crowd clapping and cheering", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Crowd_clapping_and_cheering.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Crowd_clapping_and_cheering.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Different_kinds_of_animals_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Drum_roll.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Crowd_clapping_and_cheering.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Level cheers of a crowd", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Level_cheers_of_a_crowd.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Level_cheers_of_a_crowd.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YA61Mry8zBwE.wav"))
