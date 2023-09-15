
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_AcJVyToQUQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A man and a woman laughing together", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_man_and_a_woman.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_man_and_a_woman.wav")))

TTA(text="A man shouting loudly", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_man_shouting_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_man_shouting_loudly.wav")))

TTA(text="A woman laughing alone", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_A_woman_laughing_alone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_A_woman_laughing_alone.wav")))

TTA(text="A child laughing joyfully", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_A_child_laughing_joyfully.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_A_child_laughing_joyfully.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_man_and_a_woman.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_man_shouting_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_A_woman_laughing_alone.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_A_child_laughing_joyfully.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_AcJVyToQUQ.wav"))
