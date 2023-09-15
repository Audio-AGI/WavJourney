
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YNeWW30WZjPc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Dog barking sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Dog_barking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Dog_barking_sound.wav")))

TTA(text="Dog growling sound", length=3, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Dog_growling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Dog_growling_sound.wav")))

TTA(text="Dog barking sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Dog_barking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Dog_barking_sound.wav")))

TTA(text="Dog growling sound", length=2, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Dog_growling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Dog_growling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Dog_barking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Dog_growling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Dog_barking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Dog_growling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Plastic rattling and clanking against a hard surface", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Plastic_rattling_and_clanking_against.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Plastic_rattling_and_clanking_against.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YNeWW30WZjPc.wav"))
