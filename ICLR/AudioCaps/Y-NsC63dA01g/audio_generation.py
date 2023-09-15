
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-NsC63dA01g/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A cat meowing", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_cat_meowing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_cat_meowing.wav")))

TTS(text="What an adorable cat! Isn't it beautiful?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_What_an_adorable_cat_Isnt.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_an_adorable_cat_Isnt.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_cat_meowing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_an_adorable_cat_Isnt.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-NsC63dA01g.wav"))
