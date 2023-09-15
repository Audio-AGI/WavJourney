
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7P0N61TVOxE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Motorboat engine running", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Motorboat_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Motorboat_engine_running.wav")))

TTA(text="Water splashes sound", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Water_splashes_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Water_splashes_sound.wav")))

TTA(text="Glasses clanking sound", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Glasses_clanking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Glasses_clanking_sound.wav")))

TTA(text="Group of people talking sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Group_of_people_talking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Group_of_people_talking_sound.wav")))

TTM(text="Woodwind instrument music playing", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Woodwind_instrument_music_playing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Woodwind_instrument_music_playing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Motorboat_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Water_splashes_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Glasses_clanking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Group_of_people_talking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Woodwind_instrument_music_playing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:5])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of engine and water gradually fading out", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_engine_and_water.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_engine_and_water.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7P0N61TVOxE.wav"))
