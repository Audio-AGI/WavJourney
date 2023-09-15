
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YH7-orYrKBeo/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Could someone attend to the baby, please?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Could_someone_attend_to_the.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Could_someone_attend_to_the.wav")))

TTS(text="Sure, I got it.", speaker_id="Male2_En", volume=-18, out_wav=os.path.join(wav_path, "fg_speech_1_Sure_I_got_it.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Sure_I_got_it.wav")))

TTA(text="Sound of someone moving towards the baby", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_someone_moving_towards.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_someone_moving_towards.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Could_someone_attend_to_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Sure_I_got_it.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_someone_moving_towards.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Baby crying in a subtle manner", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Baby_crying_in_a_subtle.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Murmur of people communicating in distant", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Murmur_of_people_communicating_in.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Baby_crying_in_a_subtle.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Murmur_of_people_communicating_in.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YH7-orYrKBeo.wav"))
