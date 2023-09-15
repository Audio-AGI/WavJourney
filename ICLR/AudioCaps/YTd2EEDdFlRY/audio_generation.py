
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YTd2EEDdFlRY/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Sometimes, life doesn't turn out to be the way we want it to be. But it is in those times, we must embrace the change.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Sometimes_life_doesnt_turn_out.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Sometimes_life_doesnt_turn_out.wav")))

TTA(text="Strumming of an acoustic guitar", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Strumming_of_an_acoustic_guitar.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Strumming_of_an_acoustic_guitar.wav")))

TTA(text="Second strumming of a guitar", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_strumming_of_a_guitar.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_strumming_of_a_guitar.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Sometimes_life_doesnt_turn_out.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Strumming_of_an_acoustic_guitar.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_strumming_of_a_guitar.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Soft instrumental music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Soft_instrumental_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of steam hissing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_steam_hissing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Soft_instrumental_music.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_steam_hissing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YTd2EEDdFlRY.wav"))
