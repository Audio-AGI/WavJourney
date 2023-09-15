
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YF7QtqKtllK0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud inhalation of a person snoring", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_inhalation_of_a_person.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_inhalation_of_a_person.wav")))

TTA(text="Short pause of breath", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Short_pause_of_breath.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Short_pause_of_breath.wav")))

TTA(text="Loud exhalation of a person snoring", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Loud_exhalation_of_a_person.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Loud_exhalation_of_a_person.wav")))

TTA(text="Short pause of breath", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Short_pause_of_breath.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Short_pause_of_breath.wav")))

TTA(text="Loud inhalation of a person snoring", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Loud_inhalation_of_a_person.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Loud_inhalation_of_a_person.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_inhalation_of_a_person.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Short_pause_of_breath.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Loud_exhalation_of_a_person.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Short_pause_of_breath.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Loud_inhalation_of_a_person.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YF7QtqKtllK0.wav"))
