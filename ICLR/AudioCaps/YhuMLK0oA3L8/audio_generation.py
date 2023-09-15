
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YhuMLK0oA3L8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Beautiful day, isn't it?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Beautiful_day_isnt_it.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Beautiful_day_isnt_it.wav")))

TTA(text="Man whistling a happy tune", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_happy_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_happy_tune.wav")))

TTM(text="Soft guitar playing a soothing melody", length=8, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Soft_guitar_playing_a_soothing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Soft_guitar_playing_a_soothing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Beautiful_day_isnt_it.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_whistling_a_happy_tune.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Soft_guitar_playing_a_soothing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YhuMLK0oA3L8.wav"))
