
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHdPSebdDxe4/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Something strange is happening...", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Something_strange_is_happening.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Something_strange_is_happening.wav")))

TTA(text="Intense growling sound", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Intense_growling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Intense_growling_sound.wav")))

TTS(text="It's getting closer!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Its_getting_closer.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Its_getting_closer.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Something_strange_is_happening.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Intense_growling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Its_getting_closer.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHdPSebdDxe4.wav"))
