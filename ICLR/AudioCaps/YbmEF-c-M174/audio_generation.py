
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YbmEF-c-M174/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Duck quacking repeatedly", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Duck_quacking_repeatedly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Duck_quacking_repeatedly.wav")))

TTA(text="Soft thumping", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Soft_thumping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Soft_thumping.wav")))

TTA(text="Bird chirping twice", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Bird_chirping_twice.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Bird_chirping_twice.wav")))

TTS(text="What a beautiful day at the park", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_at.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_at.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Duck_quacking_repeatedly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Soft_thumping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Bird_chirping_twice.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_at.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YbmEF-c-M174.wav"))
