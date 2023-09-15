
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YPLHXGDnig4M/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Listen to this, it sounds kind of funny.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Listen_to_this_it_sounds.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Listen_to_this_it_sounds.wav")))

TTA(text="First imitation of a cat meowing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_imitation_of_a_cat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_imitation_of_a_cat.wav")))

TTA(text="Second imitation of a cat meowing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_imitation_of_a_cat.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_imitation_of_a_cat.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Listen_to_this_it_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_imitation_of_a_cat.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_imitation_of_a_cat.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YPLHXGDnig4M.wav"))
