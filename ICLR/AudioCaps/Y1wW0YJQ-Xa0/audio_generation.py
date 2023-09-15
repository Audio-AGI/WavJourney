
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1wW0YJQ-Xa0/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sharp whoosh sound of compressed air spraying", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sharp_whoosh_sound_of_compressed.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sharp_whoosh_sound_of_compressed.wav")))

TTA(text="Metallic rattling sound like a tin can being shaken", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metallic_rattling_sound_like_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metallic_rattling_sound_like_a.wav")))

TTS(text="Interesting! Never seen anything like this before.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Interesting_Never_seen_anything_like.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Interesting_Never_seen_anything_like.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sharp_whoosh_sound_of_compressed.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metallic_rattling_sound_like_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Interesting_Never_seen_anything_like.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Murmur of a group of people talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Murmur_of_a_group_of.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Murmur_of_a_group_of.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1wW0YJQ-Xa0.wav"))
