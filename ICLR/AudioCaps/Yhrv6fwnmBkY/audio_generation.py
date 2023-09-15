
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yhrv6fwnmBkY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Rooster clucking", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Rooster_clucking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Rooster_clucking.wav")))

TTA(text="Dog whimpering", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Dog_whimpering.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Dog_whimpering.wav")))

TTS(text="What's going on there?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Whats_going_on_there.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Whats_going_on_there.wav")))

TTA(text="Dog barking", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Dog_barking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Dog_barking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Rooster_clucking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Dog_whimpering.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Whats_going_on_there.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Dog_barking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yhrv6fwnmBkY.wav"))
