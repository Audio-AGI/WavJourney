
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YItS07xtdi4s/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of fire igniting", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_fire_igniting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_fire_igniting.wav")))

TTA(text="Electronic beep sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep_sound.wav")))

TTA(text="Sound of footsteps running on concrete", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_footsteps_running_on.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_footsteps_running_on.wav")))

TTA(text="Footsteps continue on concrete", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Footsteps_continue_on_concrete.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Footsteps_continue_on_concrete.wav")))

TTA(text="Footsteps continue on concrete", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Footsteps_continue_on_concrete.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Footsteps_continue_on_concrete.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_fire_igniting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_footsteps_running_on.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Footsteps_continue_on_concrete.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Footsteps_continue_on_concrete.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:5])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Noise of vehicle engines idling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Noise_of_vehicle_engines_idling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[4:5])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Honking horns sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Honking_horns_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Noise_of_vehicle_engines_idling.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Honking_horns_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YItS07xtdi4s.wav"))
