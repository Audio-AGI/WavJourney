
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YZY4aGEniU_E/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Food and oil sizzling", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Food_and_oil_sizzling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Food_and_oil_sizzling.wav")))

TTA(text="Oil popping sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Oil_popping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Oil_popping_sound.wav")))

TTA(text="Steam hissing sound", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Steam_hissing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Steam_hissing_sound.wav")))

TTS(text="This is a culinary delight. Listen to the symphony of kitchen sounds enhancing the flavor and aroma of our dish.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_a_culinary_delight.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_a_culinary_delight.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Food_and_oil_sizzling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Oil_popping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Steam_hissing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_a_culinary_delight.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTM(text="Soft, light instrumental music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Soft_light_instrumental_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Light rattle of kitchen utensils", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Light_rattle_of_kitchen_utensils.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Soft_light_instrumental_music.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Light_rattle_of_kitchen_utensils.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YZY4aGEniU_E.wav"))
