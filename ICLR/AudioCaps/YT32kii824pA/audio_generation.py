
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YT32kii824pA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Plastic cranking noise", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Plastic_cranking_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Plastic_cranking_noise.wav")))

TTA(text="Metal rattling noise", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_rattling_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_rattling_noise.wav")))

TTS(text="The process is not as complicated as it looks. With just a few simple steps, anyone can perform it.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_The_process_is_not_as.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_process_is_not_as.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Plastic_cranking_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_rattling_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_process_is_not_as.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Series of metal objects falling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Series_of_metal_objects_falling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Series_of_metal_objects_falling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YT32kii824pA.wav"))
