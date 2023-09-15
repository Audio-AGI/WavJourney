
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_9mgOkzm-xg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Just cooking some food over here!", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Just_cooking_some_food_over.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Just_cooking_some_food_over.wav")))

TTA(text="Wood clanks on a metal pan", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Wood_clanks_on_a_metal.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Wood_clanks_on_a_metal.wav")))

TTA(text="Gravel crunching sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Gravel_crunching_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Gravel_crunching_sound.wav")))

TTA(text="Sizzling of food and oil", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sizzling_of_food_and_oil.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sizzling_of_food_and_oil.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Just_cooking_some_food_over.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Wood_clanks_on_a_metal.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Gravel_crunching_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sizzling_of_food_and_oil.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Wood clanking on a metal pan", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Wood_clanking_on_a_metal.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Gravel crunching sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Gravel_crunching_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Food sizzling in oil", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Food_sizzling_in_oil.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Wood_clanking_on_a_metal.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Gravel_crunching_sound.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Food_sizzling_in_oil.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_9mgOkzm-xg.wav"))
