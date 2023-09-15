
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yc0V_HAul7rI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Group of people laughing", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing.wav")))

TTS(text="What a wonderful moment this is!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_What_a_wonderful_moment_this.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_What_a_wonderful_moment_this.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_What_a_wonderful_moment_this.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yc0V_HAul7rI.wav"))
