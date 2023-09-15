
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YOxUVcZmeiyI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Clock ticking", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking.wav")))

TTA(text="Cuckoo bird cooing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Cuckoo_bird_cooing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Cuckoo_bird_cooing.wav")))

TTM(text="Soft and calming ambient music", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_music_0_Soft_and_calming_ambient_music.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Soft_and_calming_ambient_music.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Cuckoo_bird_cooing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Soft_and_calming_ambient_music.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YOxUVcZmeiyI.wav"))
