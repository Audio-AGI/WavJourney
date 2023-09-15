
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y3qrVku794u0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello there. Now hear the little gentleman.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_there_Now_hear_the.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_there_Now_hear_the.wav")))

TTS(text="Good day, sir.", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Good_day_sir.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Good_day_sir.wav")))

TTS(text="What a polite young man.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_What_a_polite_young_man.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_What_a_polite_young_man.wav")))

TTA(text="Sound of plastic rattling", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_plastic_rattling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_plastic_rattling.wav")))

TTA(text="Electronic beep sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_there_Now_hear_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Good_day_sir.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_What_a_polite_young_man.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_plastic_rattling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y3qrVku794u0.wav"))
