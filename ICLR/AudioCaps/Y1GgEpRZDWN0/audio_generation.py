
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1GgEpRZDWN0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This dialogue is the conversation of the woman and the man, going on for the duration of 10 seconds", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_dialogue_is_the_conversation.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_dialogue_is_the_conversation.wav")))

TTS(text="This dialogue is the continuation of the conversation of the woman and the man, continuing for the duration of 10 seconds", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_This_dialogue_is_the_continuation.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_This_dialogue_is_the_continuation.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_dialogue_is_the_conversation.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_This_dialogue_is_the_continuation.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Low murmur of the soft voice of the second man", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Low_murmur_of_the_soft.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="The subtle rustle of papers shuffling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_The_subtle_rustle_of_papers.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Low_murmur_of_the_soft.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_The_subtle_rustle_of_papers.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1GgEpRZDWN0.wav"))
