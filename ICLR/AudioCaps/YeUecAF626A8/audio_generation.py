
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YeUecAF626A8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Engine hums softly", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Engine_hums_softly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Engine_hums_softly.wav")))

TTA(text="Engine vibration sound", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Engine_vibration_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Engine_vibration_sound.wav")))

TTA(text="Engine revving sound with increasing intensity", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Engine_revving_sound_with_increasing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Engine_revving_sound_with_increasing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Engine_hums_softly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Engine_vibration_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Engine_revving_sound_with_increasing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YeUecAF626A8.wav"))
