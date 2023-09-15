
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yne2DpKCIr4Y/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Inaudible speech faintly heard from a distance", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Inaudible_speech_faintly_heard_from.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Inaudible_speech_faintly_heard_from.wav")))

TTA(text="Fast forward sound effect to fit all events within 10 seconds", length=10, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Fast_forward_sound_effect_to.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Fast_forward_sound_effect_to.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Inaudible_speech_faintly_heard_from.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Fast_forward_sound_effect_to.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of ocean waves crashing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_ocean_waves_crashing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of water streaming", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_water_streaming.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of wind blowing into a microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Sound_of_wind_blowing_into.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_ocean_waves_crashing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_water_streaming.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Sound_of_wind_blowing_into.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yne2DpKCIr4Y.wav"))
