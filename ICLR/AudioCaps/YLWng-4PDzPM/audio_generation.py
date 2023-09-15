
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YLWng-4PDzPM/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="A gentle instrumental music", length=6, volume=-20, out_wav=os.path.join(wav_path, "fg_music_0_A_gentle_instrumental_music.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_A_gentle_instrumental_music.wav")))

TTA(text="Sound of heavy fabric being rustled", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_heavy_fabric_being.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_heavy_fabric_being.wav")))

TTA(text="Melodious whistle of a man", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Melodious_whistle_of_a_man.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Melodious_whistle_of_a_man.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_A_gentle_instrumental_music.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_heavy_fabric_being.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Melodious_whistle_of_a_man.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YLWng-4PDzPM.wav"))
