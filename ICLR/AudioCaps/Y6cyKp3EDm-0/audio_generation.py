
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6cyKp3EDm-0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of pigeons pecking", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_pigeons_pecking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_pigeons_pecking.wav")))

TTA(text="Sound of pigeons cooing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_pigeons_cooing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_pigeons_cooing.wav")))

TTA(text="Sound of pigeons flapping their wings", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_pigeons_flapping_their.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_pigeons_flapping_their.wav")))

TTS(text="What a beautiful scene of nature", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_beautiful_scene_of.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_scene_of.wav")))

TTA(text="Silence", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Silence.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Silence.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_pigeons_pecking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_pigeons_cooing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_pigeons_flapping_their.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_scene_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Silence.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6cyKp3EDm-0.wav"))
