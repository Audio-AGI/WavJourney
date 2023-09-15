
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YSQHYl2Kp5ww/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I'm so glad we finally got this grill lit up.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Im_so_glad_we_finally.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Im_so_glad_we_finally.wav")))

TTA(text="Sizzling sound, similar to a steak over a hot grill", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sizzling_sound_similar_to_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sizzling_sound_similar_to_a.wav")))

TTS(text="Yeah, nothing beats a perfectly grilled steak.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yeah_nothing_beats_a_perfectly.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yeah_nothing_beats_a_perfectly.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Im_so_glad_we_finally.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sizzling_sound_similar_to_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yeah_nothing_beats_a_perfectly.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Mild instrumental music with a slow tempo", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Mild_instrumental_music_with_a.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Crackling sound, similar to wood burning in a fire", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crackling_sound_similar_to_wood.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Subtle metal scraping sound, similar to a spatula on a grill", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Subtle_metal_scraping_sound_similar.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Mild_instrumental_music_with_a.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crackling_sound_similar_to_wood.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Subtle_metal_scraping_sound_similar.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YSQHYl2Kp5ww.wav"))
