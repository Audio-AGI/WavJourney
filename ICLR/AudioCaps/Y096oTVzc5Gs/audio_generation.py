
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y096oTVzc5Gs/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Where did I leave my keys?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Where_did_I_leave_my.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Where_did_I_leave_my.wav")))

TTA(text="Rummaging sound, searching through bag", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rummaging_sound_searching_through_bag.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rummaging_sound_searching_through_bag.wav")))

TTA(text="Frustrated groaning sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Frustrated_groaning_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Frustrated_groaning_sound.wav")))

TTA(text="Grunting sound, lifting something heavy", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Grunting_sound_lifting_something_heavy.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Grunting_sound_lifting_something_heavy.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Where_did_I_leave_my.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rummaging_sound_searching_through_bag.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Frustrated_groaning_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Grunting_sound_lifting_something_heavy.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y096oTVzc5Gs.wav"))
