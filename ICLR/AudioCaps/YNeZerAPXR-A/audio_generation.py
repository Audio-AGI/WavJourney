
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YNeZerAPXR-A/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A man and a woman laughing for two seconds", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_man_and_a_woman.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_man_and_a_woman.wav")))

TTS(text="Interesting conversation follows", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Interesting_conversation_follows.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Interesting_conversation_follows.wav")))

TTS(text="Continuation of conversation", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Continuation_of_conversation.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Continuation_of_conversation.wav")))

TTA(text="Applause, someone claps", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Applause_someone_claps.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Applause_someone_claps.wav")))

TTS(text="Continuation of man's dialogue", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_2_Continuation_of_mans_dialogue.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Continuation_of_mans_dialogue.wav")))

TTS(text="Continuation of woman's dialogue", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_3_Continuation_of_womans_dialogue.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_Continuation_of_womans_dialogue.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_man_and_a_woman.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Interesting_conversation_follows.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Continuation_of_conversation.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Applause_someone_claps.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Continuation_of_mans_dialogue.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_Continuation_of_womans_dialogue.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[4:6])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Jingling bell starts", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Jingling_bell_starts.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Jingling_bell_starts.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YNeZerAPXR-A.wav"))
