
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2RjqBRzmxaM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is the beginning of a wonderful journey where we will explore the deepest secrets of the universe.", speaker_id="Female1_En", volume=-23, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_the_beginning_of.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_the_beginning_of.wav")))

TTA(text="Sound of the first few raindrops falling", length=4, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_the_first_few.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_the_first_few.wav")))

TTA(text="Sound of raindrops hitting a surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_raindrops_hitting_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_raindrops_hitting_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_the_beginning_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_the_first_few.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_raindrops_hitting_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Instrumental music playing softly in the background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Instrumental_music_playing_softly_in.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Overall sound of rain pouring", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Overall_sound_of_rain_pouring.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Instrumental_music_playing_softly_in.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Overall_sound_of_rain_pouring.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2RjqBRzmxaM.wav"))
