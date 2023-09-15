
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YR4fXcbWFhJg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I was standing there, then suddenly...", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_was_standing_there_then.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_was_standing_there_then.wav")))

TTS(text="HEY! YOU!", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_HEY_YOU.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_HEY_YOU.wav")))

TTS(text="GET OUT OF HERE!", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_2_GET_OUT_OF_HERE.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_GET_OUT_OF_HERE.wav")))

TTA(text="Sound of wind blowing into a microphone", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_wind_blowing_into.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_wind_blowing_into.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_was_standing_there_then.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_HEY_YOU.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_GET_OUT_OF_HERE.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_wind_blowing_into.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_birds_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_birds_chirping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YR4fXcbWFhJg.wav"))
