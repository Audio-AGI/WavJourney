
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YAtkD-3GjXMw/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="Fast tempo background music", length=10, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Fast_tempo_background_music.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Fast_tempo_background_music.wav")))

TTA(text="Machine gun sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Machine_gun_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Machine_gun_sound.wav")))

TTA(text="Another machine gun sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Another_machine_gun_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Another_machine_gun_sound.wav")))

TTA(text="Yet another machine gun sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Yet_another_machine_gun_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Yet_another_machine_gun_sound.wav")))

TTA(text="And a final machine gun sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_And_a_final_machine_gun.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_And_a_final_machine_gun.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Fast_tempo_background_music.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Machine_gun_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Another_machine_gun_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Yet_another_machine_gun_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_And_a_final_machine_gun.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YAtkD-3GjXMw.wav"))
