
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yj0KvrVE_Oww/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Isn't it a wonderful day today?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Isnt_it_a_wonderful_day.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Isnt_it_a_wonderful_day.wav")))

TTS(text="Indeed, it is! Better than yesterday at least.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Indeed_it_is_Better_than.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Indeed_it_is_Better_than.wav")))

TTA(text="Small horn blowing", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Small_horn_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Small_horn_blowing.wav")))

TTA(text="Sound of clattering", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_clattering.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_clattering.wav")))

TTS(text="Isn't it a wonderful day today?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Isnt_it_a_wonderful_day.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Isnt_it_a_wonderful_day.wav")))

TTS(text="Indeed, it is! Better than yesterday at least.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_3_Indeed_it_is_Better_than.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_Indeed_it_is_Better_than.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Isnt_it_a_wonderful_day.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Indeed_it_is_Better_than.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Small_horn_blowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_clattering.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Isnt_it_a_wonderful_day.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_Indeed_it_is_Better_than.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[4:6])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Subtle city ambiance, distant traffic", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Subtle_city_ambiance_distant_traffic.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Subtle_city_ambiance_distant_traffic.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yj0KvrVE_Oww.wav"))
