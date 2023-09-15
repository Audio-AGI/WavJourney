
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y473wBEwC35M/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I have been thinking about this for a while now...", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_I_have_been_thinking_about.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_have_been_thinking_about.wav")))

TTS(text="...but it's pretty clear", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_but_its_pretty_clear.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_but_its_pretty_clear.wav")))

TTA(text="Short pause", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Short_pause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Short_pause.wav")))

TTS(text="We need to find a better way to move forward.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_We_need_to_find_a.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_We_need_to_find_a.wav")))

TTS(text="That's all I have to say for now.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_3_Thats_all_I_have_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_Thats_all_I_have_to.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_have_been_thinking_about.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_but_its_pretty_clear.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Short_pause.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_We_need_to_find_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_Thats_all_I_have_to.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Distant sound of a vehicle horn honking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_sound_of_a_vehicle.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[4:5])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Distant murmuring of another man talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Distant_murmuring_of_another_man.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_sound_of_a_vehicle.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Distant_murmuring_of_another_man.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y473wBEwC35M.wav"))
