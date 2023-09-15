
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2ABngPM3raQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is a very interesting thing. You won't believe what happened next.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_a_very_interesting.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_a_very_interesting.wav")))

TTA(text="Frogs croaking", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Frogs_croaking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Frogs_croaking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_a_very_interesting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Frogs_croaking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Bongo drums playing rhythmically", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Bongo_drums_playing_rhythmically.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Bongo_drums_playing_rhythmically.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2ABngPM3raQ.wav"))
