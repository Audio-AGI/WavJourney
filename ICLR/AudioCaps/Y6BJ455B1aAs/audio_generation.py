
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6BJ455B1aAs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rocket whooshing by at a high speed", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rocket_whooshing_by_at_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rocket_whooshing_by_at_a.wav")))

TTA(text="Loud explosion with rich bass", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Loud_explosion_with_rich_bass.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Loud_explosion_with_rich_bass.wav")))

TTA(text="Truck engine running idle", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Truck_engine_running_idle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Truck_engine_running_idle.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rocket_whooshing_by_at_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Loud_explosion_with_rich_bass.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Truck_engine_running_idle.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Fire crackling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Fire_crackling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Fire_crackling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6BJ455B1aAs.wav"))
