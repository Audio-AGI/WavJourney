
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ypaf0nyjg1Js/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="The food is cooking. Can you hear the sizzle?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_The_food_is_cooking_Can.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_food_is_cooking_Can.wav")))

TTA(text="Porcelain plate clanking against table surface", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Porcelain_plate_clanking_against_table.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Porcelain_plate_clanking_against_table.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_food_is_cooking_Can.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Porcelain_plate_clanking_against_table.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Sound of cooking, oil sizzling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_cooking_oil_sizzling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_cooking_oil_sizzling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ypaf0nyjg1Js.wav"))
