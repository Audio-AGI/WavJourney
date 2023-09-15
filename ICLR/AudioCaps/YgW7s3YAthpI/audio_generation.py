
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YgW7s3YAthpI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Chewing sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Chewing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Chewing_sound.wav")))

TTA(text="Sound of liquid being poured", length=5, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_liquid_being_poured.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_liquid_being_poured.wav")))

TTA(text="Light banging sound on a hard surface", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Light_banging_sound_on_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Light_banging_sound_on_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Chewing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_liquid_being_poured.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Light_banging_sound_on_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YgW7s3YAthpI.wav"))
