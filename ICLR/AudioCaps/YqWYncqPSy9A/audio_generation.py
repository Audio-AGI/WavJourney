
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YqWYncqPSy9A/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="The evening is so calm, don't you think?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_The_evening_is_so_calm.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_evening_is_so_calm.wav")))

TTA(text="Sudden woman's laughter", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sudden_womans_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sudden_womans_laughter.wav")))

TTS(text="Indeed, it makes me feel at peace.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Indeed_it_makes_me_feel.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Indeed_it_makes_me_feel.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_evening_is_so_calm.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sudden_womans_laughter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Indeed_it_makes_me_feel.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Insect buzzing sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Insect_buzzing_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Insect_buzzing_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YqWYncqPSy9A.wav"))
