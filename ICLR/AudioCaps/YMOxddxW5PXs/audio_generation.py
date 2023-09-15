
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMOxddxW5PXs/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="The best thing about cooking is the beautiful fusion of flavors. It's almost like creating art.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_The_best_thing_about_cooking.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_best_thing_about_cooking.wav")))

TTA(text="Food being flipped in a pan", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Food_being_flipped_in_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Food_being_flipped_in_a.wav")))

TTS(text="And the result is always a symphony of tastes and textures.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_And_the_result_is_always.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_And_the_result_is_always.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_best_thing_about_cooking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Food_being_flipped_in_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_And_the_result_is_always.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sizzle sound of food frying", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sizzle_sound_of_food_frying.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of stirring utensil against cooking pot", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_stirring_utensil_against.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sizzle_sound_of_food_frying.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_stirring_utensil_against.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMOxddxW5PXs.wav"))
