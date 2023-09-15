
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YcK2kSVR1d2o/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Firework rocket launching sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Firework_rocket_launching_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Firework_rocket_launching_sound.wav")))

TTA(text="Firework explosion, pops and crackles", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Firework_explosion_pops_and_crackles.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Firework_explosion_pops_and_crackles.wav")))

TTA(text="Faint sound of firework fallout", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Faint_sound_of_firework_fallout.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Faint_sound_of_firework_fallout.wav")))

TTA(text="Second firework rocket launching sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Second_firework_rocket_launching_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Second_firework_rocket_launching_sound.wav")))

TTA(text="Second firework explosion, pops and crackles", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Second_firework_explosion_pops_and.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Second_firework_explosion_pops_and.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Firework_rocket_launching_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Firework_explosion_pops_and_crackles.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Faint_sound_of_firework_fallout.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Second_firework_rocket_launching_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Second_firework_explosion_pops_and.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YcK2kSVR1d2o.wav"))
