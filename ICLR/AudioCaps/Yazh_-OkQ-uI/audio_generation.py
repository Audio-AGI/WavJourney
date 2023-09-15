
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yazh_-OkQ-uI/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="These goats are quite lively today, aren't they?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_These_goats_are_quite_lively.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_These_goats_are_quite_lively.wav")))

TTA(text="Footsteps on gravel", length=2, volume=-35, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Footsteps_on_gravel.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_on_gravel.wav")))

TTS(text="Yes, they are. And look, a plane is passing by.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_they_are_And_look.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_they_are_And_look.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_These_goats_are_quite_lively.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_on_gravel.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_they_are_And_look.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Live goats baaing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Live_goats_baaing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Airplane flying in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Airplane_flying_in_the_distance.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Live_goats_baaing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Airplane_flying_in_the_distance.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yazh_-OkQ-uI.wav"))
