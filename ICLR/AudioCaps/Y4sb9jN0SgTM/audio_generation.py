
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4sb9jN0SgTM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Car engine revving loudly", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Car_engine_revving_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_revving_loudly.wav")))

TTS(text="Seems like a powerful engine.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Seems_like_a_powerful_engine.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Seems_like_a_powerful_engine.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_revving_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Seems_like_a_powerful_engine.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4sb9jN0SgTM.wav"))
