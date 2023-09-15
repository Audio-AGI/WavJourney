
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCfxWJ1Qoufg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is the recycling process of paper and plastic materials.", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_the_recycling_process.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_the_recycling_process.wav")))

TTA(text="Crinkling sound of paper", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Crinkling_sound_of_paper.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Crinkling_sound_of_paper.wav")))

TTA(text="Plastic creaking sound", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_creaking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_creaking_sound.wav")))

TTA(text="Sound of a toilet flushing", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_toilet_flushing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_toilet_flushing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_the_recycling_process.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Crinkling_sound_of_paper.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_creaking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_toilet_flushing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCfxWJ1Qoufg.wav"))
