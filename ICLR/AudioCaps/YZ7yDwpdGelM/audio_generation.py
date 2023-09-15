
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YZ7yDwpdGelM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is a demonstration of multiple sound effects occurring sequentially.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_a_demonstration_of.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_a_demonstration_of.wav")))

TTA(text="Sawing sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sawing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sawing_sound.wav")))

TTA(text="Metal click sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_click_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_click_sound.wav")))

TTA(text="Plastic crinkling sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Plastic_crinkling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Plastic_crinkling_sound.wav")))

TTA(text="Silent pause", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Silent_pause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Silent_pause.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_a_demonstration_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sawing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_click_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Plastic_crinkling_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Silent_pause.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[4:5])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Sound of water trickling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_trickling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[4:5])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Sound of wind blowing into a microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_wind_blowing_into.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_trickling.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_wind_blowing_into.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YZ7yDwpdGelM.wav"))
