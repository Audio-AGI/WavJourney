
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y8nUqSYC66mI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of person screaming", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_person_screaming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_person_screaming.wav")))

TTS(text="Oh, wow!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Oh_wow.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Oh_wow.wav")))

TTA(text="Sound of person laughing", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_person_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_person_laughing.wav")))

TTS(text="That was fun!", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_That_was_fun.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_That_was_fun.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_person_screaming.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Oh_wow.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_person_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_That_was_fun.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of water splashing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_splashing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_splashing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y8nUqSYC66mI.wav"))
