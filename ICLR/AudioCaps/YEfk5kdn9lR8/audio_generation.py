
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YEfk5kdn9lR8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I think I will go outside to play now.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_think_I_will_go.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_think_I_will_go.wav")))

TTA(text="Sound of a door creaking open slowly", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_door_creaking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_door_creaking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_think_I_will_go.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_door_creaking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YEfk5kdn9lR8.wav"))
