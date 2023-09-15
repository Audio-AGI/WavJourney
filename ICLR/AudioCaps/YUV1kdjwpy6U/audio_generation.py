
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YUV1kdjwpy6U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Vehicle engine running", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_running.wav")))

TTA(text="Vehicle engine powering down", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Vehicle_engine_powering_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_engine_powering_down.wav")))

TTS(text="I've never seen anything like this before", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Ive_never_seen_anything_like.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ive_never_seen_anything_like.wav")))

TTA(text="Short static noise", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Short_static_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Short_static_noise.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Vehicle_engine_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Vehicle_engine_powering_down.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ive_never_seen_anything_like.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Short_static_noise.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YUV1kdjwpy6U.wav"))
