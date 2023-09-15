
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7QN3lwOzfdg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of dialing and calling a number from a telephone", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_dialing_and_calling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_dialing_and_calling.wav")))

TTS(text="Hello there, I just dialed your number", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_there_I_just_dialed.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_there_I_just_dialed.wav")))

TTS(text="Hey, I see you managed to reach me. What's up?", speaker_id="Male2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Hey_I_see_you_managed.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hey_I_see_you_managed.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_dialing_and_calling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_there_I_just_dialed.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hey_I_see_you_managed.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Telephone ringing sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Telephone_ringing_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Telephone_ringing_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7QN3lwOzfdg.wav"))
