
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPMMkPq5jJXY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of person burping", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_person_burping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_person_burping.wav")))

TTS(text="That's hilarious!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Thats_hilarious.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Thats_hilarious.wav")))

TTS(text="Can't stop burping... Excuse me!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Cant_stop_burping_Excuse_me.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Cant_stop_burping_Excuse_me.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_person_burping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Thats_hilarious.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Cant_stop_burping_Excuse_me.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Continuous burping sounds", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_burping_sounds.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_burping_sounds.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPMMkPq5jJXY.wav"))
