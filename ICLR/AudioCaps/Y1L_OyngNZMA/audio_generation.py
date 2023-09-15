
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1L_OyngNZMA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Ladies and gentlemen, thank you for coming here tonight!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_thank_you.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_thank_you.wav")))

TTA(text="Laughter of a crowd", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_a_crowd.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_a_crowd.wav")))

TTA(text="Excited shouts from a crowd", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Excited_shouts_from_a_crowd.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Excited_shouts_from_a_crowd.wav")))

TTA(text="Clapping of a crowd", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Clapping_of_a_crowd.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Clapping_of_a_crowd.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_thank_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_a_crowd.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Excited_shouts_from_a_crowd.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Clapping_of_a_crowd.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1L_OyngNZMA.wav"))
