
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YK2kIOBeCfuo/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Good evening everyone, here's a joke for you all...", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Good_evening_everyone_heres_a.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Good_evening_everyone_heres_a.wav")))

TTA(text="Crowd laughing sound effect", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Crowd_laughing_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Crowd_laughing_sound_effect.wav")))

TTA(text="Crowd applause sound effect", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Crowd_applause_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Crowd_applause_sound_effect.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Good_evening_everyone_heres_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Crowd_laughing_sound_effect.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Crowd_applause_sound_effect.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YK2kIOBeCfuo.wav"))
