
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4_DjmCg8Ra8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rapid gunfire, multiple shots fired off", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rapid_gunfire_multiple_shots_fired.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rapid_gunfire_multiple_shots_fired.wav")))

TTA(text="Echoing effect of gunfire", length=3, volume=-35, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Echoing_effect_of_gunfire.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Echoing_effect_of_gunfire.wav")))

TTS(text="Everyone, get down!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Everyone_get_down.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Everyone_get_down.wav")))

TTA(text="Final gunshot, single and loud", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Final_gunshot_single_and_loud.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Final_gunshot_single_and_loud.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rapid_gunfire_multiple_shots_fired.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Echoing_effect_of_gunfire.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Everyone_get_down.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Final_gunshot_single_and_loud.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4_DjmCg8Ra8.wav"))
