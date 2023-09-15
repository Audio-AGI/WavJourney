
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YeYbFtxZmKL4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Horses trotting", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Horses_trotting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Horses_trotting.wav")))

TTA(text="Wood clanking, first time", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Wood_clanking_first_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Wood_clanking_first_time.wav")))

TTA(text="Wood clanking, second time", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Wood_clanking_second_time.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Wood_clanking_second_time.wav")))

TTS(text="Such a beautiful day to enjoy the outdoors. Listen to the horses trot, and the birds chirp.", speaker_id="Female2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Such_a_beautiful_day_to.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Such_a_beautiful_day_to.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Horses_trotting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Wood_clanking_first_time.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Wood_clanking_second_time.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Such_a_beautiful_day_to.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Birds chirping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing into a microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing_into_a_microphone.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing_into_a_microphone.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YeYbFtxZmKL4.wav"))
