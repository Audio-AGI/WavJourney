
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yos_2U4xqTqw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud explosion sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_explosion_sound.wav")))

TTA(text="Gunfire sound, multiple shots", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Gunfire_sound_multiple_shots.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Gunfire_sound_multiple_shots.wav")))

TTS(text="Stay calm and find shelter!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Stay_calm_and_find_shelter.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Stay_calm_and_find_shelter.wav")))

TTA(text="Another loud explosion sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Another_loud_explosion_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Another_loud_explosion_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_explosion_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Gunfire_sound_multiple_shots.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Stay_calm_and_find_shelter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Another_loud_explosion_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yos_2U4xqTqw.wav"))
