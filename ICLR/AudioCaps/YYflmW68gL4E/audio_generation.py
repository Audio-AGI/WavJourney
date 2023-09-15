
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YYflmW68gL4E/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a person burping", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_person_burping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_person_burping.wav")))

TTA(text="Laughter sound effect", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughter_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughter_sound_effect.wav")))

TTS(text="Well, isn't that charming!", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Well_isnt_that_charming.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Well_isnt_that_charming.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_person_burping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughter_sound_effect.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Well_isnt_that_charming.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YYflmW68gL4E.wav"))
