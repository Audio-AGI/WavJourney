
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YpuZL08fzpXk/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Close gunshot, single", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Close_gunshot_single.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Close_gunshot_single.wav")))

TTS(text="I've got a visual on the target", speaker_id="Male1_En", volume=-18, out_wav=os.path.join(wav_path, "fg_speech_0_Ive_got_a_visual_on.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ive_got_a_visual_on.wav")))

TTA(text="Sudden large boom sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sudden_large_boom_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sudden_large_boom_sound.wav")))

TTS(text="Affirmative, keep your position", speaker_id="Male2_En", volume=-16, out_wav=os.path.join(wav_path, "fg_speech_1_Affirmative_keep_your_position.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Affirmative_keep_your_position.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Close_gunshot_single.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ive_got_a_visual_on.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sudden_large_boom_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Affirmative_keep_your_position.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sounds of distant gunshots", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sounds_of_distant_gunshots.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sounds_of_distant_gunshots.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YpuZL08fzpXk.wav"))
