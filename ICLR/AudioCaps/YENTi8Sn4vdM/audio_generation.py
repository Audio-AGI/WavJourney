
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YENTi8Sn4vdM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Look, the water is splashing all over!", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Look_the_water_is_splashing.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Look_the_water_is_splashing.wav")))

TTS(text="Yes, dear. It's very beautiful, right?", speaker_id="Female1_En", volume=-17, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_dear_Its_very_beautiful.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_dear_Its_very_beautiful.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Look_the_water_is_splashing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_dear_Its_very_beautiful.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Soft splashing of water", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Soft_splashing_of_water.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Soft_splashing_of_water.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YENTi8Sn4vdM.wav"))
