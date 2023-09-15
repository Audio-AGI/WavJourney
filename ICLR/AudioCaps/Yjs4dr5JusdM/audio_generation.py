
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yjs4dr5JusdM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Could you please come a little closer?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Could_you_please_come_a.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Could_you_please_come_a.wav")))

TTS(text="Why do I need to come closer?", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Why_do_I_need_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Why_do_I_need_to.wav")))

TTS(text="Just wondering if we could have a more intimate talk.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_2_Just_wondering_if_we_could.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Just_wondering_if_we_could.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Could_you_please_come_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Why_do_I_need_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Just_wondering_if_we_could.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yjs4dr5JusdM.wav"))
