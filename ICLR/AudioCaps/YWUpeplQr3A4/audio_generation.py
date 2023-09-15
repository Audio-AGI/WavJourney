
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YWUpeplQr3A4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud shrill sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_shrill_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_shrill_sound.wav")))

TTA(text="Power tool drilling", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Power_tool_drilling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Power_tool_drilling.wav")))

TTS(text="Ahhhhhhhhhhh!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Ahhhhhhhhhhh.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ahhhhhhhhhhh.wav")))

TTA(text="Liquid splattering sound effect", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Liquid_splattering_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Liquid_splattering_sound_effect.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_shrill_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Power_tool_drilling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ahhhhhhhhhhh.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Liquid_splattering_sound_effect.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Sound of liquid pouring", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_liquid_pouring.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_liquid_pouring.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YWUpeplQr3A4.wav"))
