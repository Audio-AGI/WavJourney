
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YBXxlqaDvdaA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish.", speaker_id="Old_Man_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_He_was_an_old_man.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/elder_morgen.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_He_was_an_old_man.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_He_was_an_old_man.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Ocean waves trickling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Ocean_waves_trickling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Ocean waves splashing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Ocean_waves_splashing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing into a microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Wind_blowing_into_a_microphone.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Ocean_waves_trickling.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Ocean_waves_splashing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Wind_blowing_into_a_microphone.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YBXxlqaDvdaA.wav"))
