
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YJdFmMw0zyKA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Look at Max go!", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Look_at_Max_go.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Look_at_Max_go.wav")))

TTA(text="Dog barking sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Dog_barking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Dog_barking_sound.wav")))

TTA(text="Splash sound in a pool", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Splash_sound_in_a_pool.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Splash_sound_in_a_pool.wav")))

TTA(text="Children laughing sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Children_laughing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Children_laughing_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Look_at_Max_go.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Dog_barking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Splash_sound_in_a_pool.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Children_laughing_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YJdFmMw0zyKA.wav"))
