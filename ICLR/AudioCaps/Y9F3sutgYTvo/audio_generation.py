
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9F3sutgYTvo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Man yelling", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_yelling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_yelling.wav")))

TTA(text="Infant crying", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Infant_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Infant_crying.wav")))

TTS(text="Stop that noise, now!", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Stop_that_noise_now.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Stop_that_noise_now.wav")))

TTA(text="Laugh track", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Laugh_track.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Laugh_track.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_yelling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Infant_crying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Stop_that_noise_now.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Laugh_track.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Crowd of people talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_talking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9F3sutgYTvo.wav"))
