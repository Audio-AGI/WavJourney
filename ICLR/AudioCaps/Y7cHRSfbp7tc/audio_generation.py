
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7cHRSfbp7tc/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="First knock sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_knock_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_knock_sound.wav")))

TTA(text="Second knock sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_knock_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_knock_sound.wav")))

TTA(text="Third knock sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Third_knock_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Third_knock_sound.wav")))

TTA(text="Fourth knock sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Fourth_knock_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Fourth_knock_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_knock_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_knock_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Third_knock_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Fourth_knock_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Indistinct chatter, people talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Indistinct_chatter_people_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Indistinct_chatter_people_talking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7cHRSfbp7tc.wav"))
