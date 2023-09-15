
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YOUUckswAaNI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Short hammering sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Short_hammering_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Short_hammering_sound.wav")))

TTS(text="Hey, did you hear that hammering sound?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hey_did_you_hear_that.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hey_did_you_hear_that.wav")))

TTS(text="Yes, I wonder what's going on.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_I_wonder_whats_going.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_I_wonder_whats_going.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Short_hammering_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hey_did_you_hear_that.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_I_wonder_whats_going.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YOUUckswAaNI.wav"))
