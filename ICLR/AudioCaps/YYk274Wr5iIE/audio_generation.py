
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YYk274Wr5iIE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle driving by while splashing water", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_driving_by_while_splashing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_driving_by_while_splashing.wav")))

TTA(text="Stream of water trickling and flowing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Stream_of_water_trickling_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Stream_of_water_trickling_and.wav")))

TTA(text="Wind blowing into a microphone", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Wind_blowing_into_a_microphone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Wind_blowing_into_a_microphone.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_driving_by_while_splashing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Stream_of_water_trickling_and.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Wind_blowing_into_a_microphone.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Distant thunder roaring", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_thunder_roaring.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_thunder_roaring.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YYk274Wr5iIE.wav"))
