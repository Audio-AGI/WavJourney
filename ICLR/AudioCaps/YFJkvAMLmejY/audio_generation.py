
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFJkvAMLmejY/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's great to see everybody here.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Its_great_to_see_everybody.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_great_to_see_everybody.wav")))

TTS(text="Isn't it? Thanks for coming.", speaker_id="Male2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Isnt_it_Thanks_for_coming.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Isnt_it_Thanks_for_coming.wav")))

TTA(text="Air horn sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Air_horn_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Air_horn_sound.wav")))

TTA(text="Laughter of a group of people", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_group_of.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_group_of.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_great_to_see_everybody.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Isnt_it_Thanks_for_coming.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Air_horn_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_group_of.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="General chatter", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_General_chatter.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_General_chatter.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFJkvAMLmejY.wav"))
