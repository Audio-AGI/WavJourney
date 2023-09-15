
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yp9qRTh4BmSE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Looks like trouble ahead.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Looks_like_trouble_ahead.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Looks_like_trouble_ahead.wav")))

TTS(text="AAAAAAAHHH!", speaker_id="Male2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_AAAAAAAHHH.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_AAAAAAAHHH.wav")))

TTA(text="Multiple gunshot sounds", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Multiple_gunshot_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Multiple_gunshot_sounds.wav")))

TTA(text="Multiple gunshot sounds", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Multiple_gunshot_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Multiple_gunshot_sounds.wav")))

TTA(text="Multiple gunshot sounds", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Multiple_gunshot_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Multiple_gunshot_sounds.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Looks_like_trouble_ahead.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_AAAAAAAHHH.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Multiple_gunshot_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Multiple_gunshot_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Multiple_gunshot_sounds.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yp9qRTh4BmSE.wav"))
