
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ylq9RvAA4mqY/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Cooking is quite a therapeutic activity, it's all about precision and patience.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Cooking_is_quite_a_therapeutic.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Cooking_is_quite_a_therapeutic.wav")))

TTA(text="Intense sizzling sound as more food is added", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Intense_sizzling_sound_as_more.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Intense_sizzling_sound_as_more.wav")))

TTS(text="The key is to keep the heat consistent.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_The_key_is_to_keep.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_The_key_is_to_keep.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Cooking_is_quite_a_therapeutic.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Intense_sizzling_sound_as_more.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_The_key_is_to_keep.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Persistent metal clanking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Persistent_metal_clanking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sizzling sound of frying food and hot bubbling oil", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sizzling_sound_of_frying_food.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Persistent_metal_clanking.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sizzling_sound_of_frying_food.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ylq9RvAA4mqY.wav"))
