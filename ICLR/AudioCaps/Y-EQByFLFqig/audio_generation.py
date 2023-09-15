
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-EQByFLFqig/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="As the rain begins to fall, we move into cover. It's a soothing sound, almost like a melody. We hold our breaths as we listen, waiting for the inevitable storm.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_As_the_rain_begins_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_As_the_rain_begins_to.wav")))

TTA(text="Thunder rumble in the distance", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Thunder_rumble_in_the_distance.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Thunder_rumble_in_the_distance.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_As_the_rain_begins_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Thunder_rumble_in_the_distance.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Light rainfall", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Light_rainfall.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Light_rainfall.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-EQByFLFqig.wav"))
