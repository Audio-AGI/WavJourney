
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1slvoNgzBLE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Subway train signal", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Subway_train_signal.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Subway_train_signal.wav")))

TTA(text="Bell chime", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Bell_chime.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Bell_chime.wav")))

TTA(text="Horn honk", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Horn_honk.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Horn_honk.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Subway_train_signal.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Bell_chime.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Horn_honk.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sounds of a crowd talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sounds_of_a_crowd_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sounds_of_a_crowd_talking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1slvoNgzBLE.wav"))
