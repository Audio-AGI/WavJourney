
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YglAeihz0NAM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Wind blowing into microphone", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Wind_blowing_into_microphone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Wind_blowing_into_microphone.wav")))

TTS(text="It's such a beautiful day today!", speaker_id="Female2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Its_such_a_beautiful_day.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_such_a_beautiful_day.wav")))

TTS(text="Yes, it's perfect beach weather.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_its_perfect_beach_weather.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_its_perfect_beach_weather.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Wind_blowing_into_microphone.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_such_a_beautiful_day.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_its_perfect_beach_weather.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Ocean waves crashing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Ocean_waves_crashing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Children laughing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Children_laughing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Ocean_waves_crashing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Children_laughing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YglAeihz0NAM.wav"))
