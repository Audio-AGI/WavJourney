
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y0NGSrwioYjA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of rustling leaves as someone walks", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_rustling_leaves_as.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_rustling_leaves_as.wav")))

TTS(text="Hello there, Little ones. How are you today?", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_there_Little_ones_How.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_there_Little_ones_How.wav")))

TTA(text="Various animal sounds in response, like chirps and squeaks", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Various_animal_sounds_in_response.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Various_animal_sounds_in_response.wav")))

TTM(text="Soft, uplifting piano music to close the scene", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_music_0_Soft_uplifting_piano_music_to.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Soft_uplifting_piano_music_to.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_rustling_leaves_as.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_there_Little_ones_How.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Various_animal_sounds_in_response.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Soft_uplifting_piano_music_to.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sounds of a peaceful woodland, birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sounds_of_a_peaceful_woodland.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sounds_of_a_peaceful_woodland.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y0NGSrwioYjA.wav"))
