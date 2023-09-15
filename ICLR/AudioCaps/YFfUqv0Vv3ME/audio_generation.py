
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFfUqv0Vv3ME/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I wonder how it's like to experience the rural life.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_I_wonder_how_its_like.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_wonder_how_its_like.wav")))

TTS(text="I believe it will be peaceful and refreshing. Let's find out.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_I_believe_it_will_be.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_I_believe_it_will_be.wav")))

TTA(text="Plastic clacking representing footsteps on grass", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_representing_footsteps_on.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_representing_footsteps_on.wav")))

TTA(text="Rooster crowing in the distance", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Rooster_crowing_in_the_distance.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Rooster_crowing_in_the_distance.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_wonder_how_its_like.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_I_believe_it_will_be.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clacking_representing_footsteps_on.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Rooster_crowing_in_the_distance.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Environmental noise of a quiet countryside", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Environmental_noise_of_a_quiet.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Environmental_noise_of_a_quiet.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFfUqv0Vv3ME.wav"))
