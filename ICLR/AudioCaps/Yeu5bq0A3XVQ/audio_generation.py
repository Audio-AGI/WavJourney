
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yeu5bq0A3XVQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Man exhaling deeply", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Man_exhaling_deeply.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Man_exhaling_deeply.wav")))

TTA(text="Man gasping for air", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Man_gasping_for_air.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Man_gasping_for_air.wav")))

TTS(text="I... I need help.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_I_need_help.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_I_need_help.wav")))

TTA(text="Man gurgling", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Man_gurgling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Man_gurgling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Man_exhaling_deeply.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Man_gasping_for_air.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_I_need_help.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Man_gurgling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yeu5bq0A3XVQ.wav"))
