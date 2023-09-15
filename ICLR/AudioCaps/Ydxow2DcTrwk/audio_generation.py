
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ydxow2DcTrwk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Strong wind blowing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Strong_wind_blowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Strong_wind_blowing.wav")))

TTS(text="What's the weather it's not looking good.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Whats_the_weather_its_not.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Whats_the_weather_its_not.wav")))

TTS(text="Yes, it seems like a storm coming up.", speaker_id="Male2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_it_seems_like_a.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_it_seems_like_a.wav")))

TTA(text="Loud burst of thunder", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_burst_of_thunder.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_burst_of_thunder.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Strong_wind_blowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Whats_the_weather_its_not.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_it_seems_like_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_burst_of_thunder.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ydxow2DcTrwk.wav"))
