
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4CAMv5nlr-0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Ladies and gentlemen, thank you, for your generous support and encouragement", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_thank_you.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_thank_you.wav")))

TTA(text="Applause and cheering", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Applause_and_cheering.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Applause_and_cheering.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_thank_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Applause_and_cheering.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4CAMv5nlr-0.wav"))
