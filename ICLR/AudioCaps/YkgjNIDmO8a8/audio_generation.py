
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YkgjNIDmO8a8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Emergency vehicle siren blasts", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Emergency_vehicle_siren_blasts.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Emergency_vehicle_siren_blasts.wav")))

TTS(text="The emergency response is on the way.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_The_emergency_response_is_on.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_emergency_response_is_on.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Emergency_vehicle_siren_blasts.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_emergency_response_is_on.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YkgjNIDmO8a8.wav"))
