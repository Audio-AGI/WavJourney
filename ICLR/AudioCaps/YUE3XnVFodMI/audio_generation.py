
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YUE3XnVFodMI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Crowd applause", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Crowd_applause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Crowd_applause.wav")))

TTS(text="Ladies and Gentlemen, thank you for your applause.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Ladies_and_Gentlemen_thank_you.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ladies_and_Gentlemen_thank_you.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Crowd_applause.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ladies_and_Gentlemen_thank_you.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YUE3XnVFodMI.wav"))
