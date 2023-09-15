
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpTJKJxaheI8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Ticking sound at regular intervals", length=7, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Ticking_sound_at_regular_intervals.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Ticking_sound_at_regular_intervals.wav")))

TTA(text="Ticking sound at short intervals", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Ticking_sound_at_short_intervals.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Ticking_sound_at_short_intervals.wav")))

TTS(text="*Coughs quietly*", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Coughs_quietly.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Coughs_quietly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Ticking_sound_at_regular_intervals.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Ticking_sound_at_short_intervals.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Coughs_quietly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpTJKJxaheI8.wav"))
