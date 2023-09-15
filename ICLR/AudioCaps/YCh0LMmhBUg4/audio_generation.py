
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCh0LMmhBUg4/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="And so, we continue our journey", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_And_so_we_continue_our.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_And_so_we_continue_our.wav")))

TTA(text="A young kid yelling, voice fading quickly", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_young_kid_yelling_voice.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_young_kid_yelling_voice.wav")))

TTA(text="Sound of an aircraft flying at a distance", length=6, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_an_aircraft_flying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_an_aircraft_flying.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_And_so_we_continue_our.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_young_kid_yelling_voice.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_an_aircraft_flying.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Constant wind blowing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Constant_wind_blowing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Constant_wind_blowing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCh0LMmhBUg4.wav"))
