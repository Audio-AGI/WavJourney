
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YVOXl8iR-HnI/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's getting really windy out here.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Its_getting_really_windy_out.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_getting_really_windy_out.wav")))

TTA(text="Sound of aircraft flying by", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_aircraft_flying_by.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_aircraft_flying_by.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_getting_really_windy_out.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_aircraft_flying_by.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Blowing gusts of wind", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Blowing_gusts_of_wind.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Blowing_gusts_of_wind.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YVOXl8iR-HnI.wav"))
