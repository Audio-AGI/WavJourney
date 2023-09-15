
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yii3Geza3hAU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Initial vibration of sewing machine starting", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Initial_vibration_of_sewing_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Initial_vibration_of_sewing_machine.wav")))

TTA(text="Short pause, no sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Short_pause_no_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Short_pause_no_sound.wav")))

TTA(text="Second burst of sewing machine vibration", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Second_burst_of_sewing_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Second_burst_of_sewing_machine.wav")))

TTA(text="Short pause, no sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Short_pause_no_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Short_pause_no_sound.wav")))

TTA(text="Final burst of sewing machine vibration", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Final_burst_of_sewing_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Final_burst_of_sewing_machine.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Initial_vibration_of_sewing_machine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Short_pause_no_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Second_burst_of_sewing_machine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Short_pause_no_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Final_burst_of_sewing_machine.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yii3Geza3hAU.wav"))
