
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YynHdcJ9Oqaw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud whoosh sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_whoosh_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_whoosh_sound.wav")))

TTA(text="Second loud whoosh sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_loud_whoosh_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_loud_whoosh_sound.wav")))

TTA(text="Third loud whoosh sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Third_loud_whoosh_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Third_loud_whoosh_sound.wav")))

TTA(text="Fourth loud whoosh sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Fourth_loud_whoosh_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Fourth_loud_whoosh_sound.wav")))

TTA(text="Fifth loud whoosh sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Fifth_loud_whoosh_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Fifth_loud_whoosh_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_whoosh_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_loud_whoosh_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Third_loud_whoosh_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Fourth_loud_whoosh_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Fifth_loud_whoosh_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YynHdcJ9Oqaw.wav"))
