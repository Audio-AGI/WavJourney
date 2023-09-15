
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpO8kbg9IJnc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Metal squeaking and clanking", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Metal_squeaking_and_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Metal_squeaking_and_clanking.wav")))

TTS(text="Hmm, that should be okay now.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Hmm_that_should_be_okay.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hmm_that_should_be_okay.wav")))

TTA(text="Faucet pouring water", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Faucet_pouring_water.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Faucet_pouring_water.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Metal_squeaking_and_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hmm_that_should_be_okay.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Faucet_pouring_water.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpO8kbg9IJnc.wav"))
