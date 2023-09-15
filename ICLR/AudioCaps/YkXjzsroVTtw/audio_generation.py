
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YkXjzsroVTtw/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's a beautiful morning, isn't it?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_morning_isnt.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_morning_isnt.wav")))

TTA(text="Footsteps on gravel", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Footsteps_on_gravel.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_on_gravel.wav")))

TTA(text="More footsteps on gravel", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_More_footsteps_on_gravel.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_More_footsteps_on_gravel.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_morning_isnt.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_on_gravel.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_More_footsteps_on_gravel.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Birds chirping in the morning", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping_in_the_morning.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping_in_the_morning.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YkXjzsroVTtw.wav"))
