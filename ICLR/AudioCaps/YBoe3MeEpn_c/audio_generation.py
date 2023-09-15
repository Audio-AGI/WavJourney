
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBoe3MeEpn_c/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Metal pan clacking against the hard surface", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Metal_pan_clacking_against_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Metal_pan_clacking_against_the.wav")))

TTA(text="Compressed air spraying sound", length=3, volume=-22, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Compressed_air_spraying_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Compressed_air_spraying_sound.wav")))

TTS(text="I'm spraying the compressed air to clean the dust, and you can hear the aerosol can tapping sound in the background", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Im_spraying_the_compressed_air.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Im_spraying_the_compressed_air.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Metal_pan_clacking_against_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Compressed_air_spraying_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Im_spraying_the_compressed_air.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Aerosol can tapping a hard surface", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Aerosol_can_tapping_a_hard.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Aerosol_can_tapping_a_hard.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBoe3MeEpn_c.wav"))
