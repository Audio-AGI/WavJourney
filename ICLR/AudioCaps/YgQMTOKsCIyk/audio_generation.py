
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YgQMTOKsCIyk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Ducks quacking and chirping", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Ducks_quacking_and_chirping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Ducks_quacking_and_chirping.wav")))

TTS(text="What a beautiful day to enjoy the nature", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_to.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Ducks_quacking_and_chirping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_beautiful_day_to.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of water trickling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_trickling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_trickling.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YgQMTOKsCIyk.wav"))
