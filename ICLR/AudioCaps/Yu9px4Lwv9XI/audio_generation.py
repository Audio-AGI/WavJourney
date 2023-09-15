
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yu9px4Lwv9XI/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="Tribal drums playing", length=10, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Tribal_drums_playing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Tribal_drums_playing.wav")))

TTA(text="Footsteps shuffling on wet dirt", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_wet_dirt.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_wet_dirt.wav")))

TTM(text="Continuation of tribal drums", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_music_1_Continuation_of_tribal_drums.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_1_Continuation_of_tribal_drums.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Tribal_drums_playing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_shuffling_on_wet_dirt.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_1_Continuation_of_tribal_drums.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Frogs chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Frogs_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Crickets chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Crickets_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Frogs_chirping.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Crickets_chirping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yu9px4Lwv9XI.wav"))
