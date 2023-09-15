
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMj_BO-iK1G4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Quick burst of vibrations from a sewing machine", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Quick_burst_of_vibrations_from.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Quick_burst_of_vibrations_from.wav")))

TTA(text="Clicking sounds of sewing machine", length=4, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Clicking_sounds_of_sewing_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Clicking_sounds_of_sewing_machine.wav")))

TTA(text="Rattling noise from sewing machine", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Rattling_noise_from_sewing_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Rattling_noise_from_sewing_machine.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Quick_burst_of_vibrations_from.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Clicking_sounds_of_sewing_machine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Rattling_noise_from_sewing_machine.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMj_BO-iK1G4.wav"))
