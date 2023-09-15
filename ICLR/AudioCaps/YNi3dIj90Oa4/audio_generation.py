
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YNi3dIj90Oa4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Multiple gunshots", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Multiple_gunshots.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Multiple_gunshots.wav")))

TTS(text="Did you hear that?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Did_you_hear_that.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Did_you_hear_that.wav")))

TTS(text="Yes, it sounded like gunshots.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_it_sounded_like_gunshots.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_it_sounded_like_gunshots.wav")))

TTM(text="Intense suspenseful music", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_music_0_Intense_suspenseful_music.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Intense_suspenseful_music.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Multiple_gunshots.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Did_you_hear_that.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_it_sounded_like_gunshots.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Intense_suspenseful_music.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YNi3dIj90Oa4.wav"))
