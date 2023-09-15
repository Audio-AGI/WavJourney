
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yr2KhpX_QgXA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's going to be a smooth ride.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Its_going_to_be_a.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_going_to_be_a.wav")))

TTS(text="We've checked everything. We are good to go.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Weve_checked_everything_We_are.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Weve_checked_everything_We_are.wav")))

TTA(text="Car engine starting and revving", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Car_engine_starting_and_revving.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_starting_and_revving.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_going_to_be_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Weve_checked_everything_We_are.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_starting_and_revving.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yr2KhpX_QgXA.wav"))
