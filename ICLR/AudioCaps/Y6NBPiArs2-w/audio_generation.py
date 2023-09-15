
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6NBPiArs2-w/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Series of rapid gunshots firing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Series_of_rapid_gunshots_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Series_of_rapid_gunshots_firing.wav")))

TTA(text="Footsteps running on concrete", length=3, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Footsteps_running_on_concrete.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Footsteps_running_on_concrete.wav")))

TTS(text="Groans in pain and distress", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Groans_in_pain_and_distress.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Groans_in_pain_and_distress.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Series_of_rapid_gunshots_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Footsteps_running_on_concrete.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Groans_in_pain_and_distress.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Muffled heartbeat sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Muffled_heartbeat_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Muffled_heartbeat_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6NBPiArs2-w.wav"))
