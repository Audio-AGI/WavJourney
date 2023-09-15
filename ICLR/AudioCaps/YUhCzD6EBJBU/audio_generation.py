
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YUhCzD6EBJBU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Fast vibration of power tool", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Fast_vibration_of_power_tool.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Fast_vibration_of_power_tool.wav")))

TTS(text="Watch your step, we're fixing the floor here.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Watch_your_step_were_fixing.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Watch_your_step_were_fixing.wav")))

TTA(text="Successive banging sounds", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Successive_banging_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Successive_banging_sounds.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Fast_vibration_of_power_tool.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Watch_your_step_were_fixing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Successive_banging_sounds.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Distant noise of construction site work", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_noise_of_construction_site.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_noise_of_construction_site.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YUhCzD6EBJBU.wav"))
