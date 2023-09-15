
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YWq4OD3olO2w/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="So, as I was saying...", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_So_as_I_was_saying.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_So_as_I_was_saying.wav")))

TTA(text="Children screaming", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Children_screaming.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Children_screaming.wav")))

TTS(text="Anyway, we need to find a solution quickly...", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Anyway_we_need_to_find.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Anyway_we_need_to_find.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_So_as_I_was_saying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Children_screaming.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Anyway_we_need_to_find.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YWq4OD3olO2w.wav"))
