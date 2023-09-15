
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1IoHRTUp86c/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Just a moment, I have something to say.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Just_a_moment_I_have.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Just_a_moment_I_have.wav")))

TTA(text="The sound of an engine running, slightly muffled", length=7, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_an_engine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_an_engine.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Just_a_moment_I_have.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_an_engine.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Distant muffled engine starting", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_muffled_engine_starting.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_muffled_engine_starting.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1IoHRTUp86c.wav"))
