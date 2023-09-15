
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YmGa2JgAiKV8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is the first man speaking.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_the_first_man.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_the_first_man.wav")))

TTS(text="This is the second man speaking.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_This_is_the_second_man.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_This_is_the_second_man.wav")))

TTS(text="This is the woman speaking.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_This_is_the_woman_speaking.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_This_is_the_woman_speaking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_the_first_man.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_This_is_the_second_man.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_This_is_the_woman_speaking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YmGa2JgAiKV8.wav"))
