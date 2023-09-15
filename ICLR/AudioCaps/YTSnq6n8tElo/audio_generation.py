
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YTSnq6n8tElo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Tapping noise on a desk", length=1.5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Tapping_noise_on_a_desk.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Tapping_noise_on_a_desk.wav")))

TTS(text="Hello, is anyone there?", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_is_anyone_there.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_is_anyone_there.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Tapping_noise_on_a_desk.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_is_anyone_there.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YTSnq6n8tElo.wav"))
