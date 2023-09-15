
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YxBZnvfniA1c/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello everyone, this is a lovely day.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_everyone_this_is_a.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_everyone_this_is_a.wav")))

TTS(text="Yes, it is!", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_it_is.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_it_is.wav")))

TTA(text="Laughter sound effect", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Laughter_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Laughter_sound_effect.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_everyone_this_is_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_it_is.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Laughter_sound_effect.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YxBZnvfniA1c.wav"))
