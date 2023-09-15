
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YoNHCc_izsDE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of water splashing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_water_splashing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_water_splashing.wav")))

TTS(text="Laughing sounds", speaker_id="Child_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Laughing_sounds.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Laughing_sounds.wav")))

TTA(text="More water splashing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_More_water_splashing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_More_water_splashing.wav")))

TTS(text="Continued laughing sounds", speaker_id="Child_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Continued_laughing_sounds.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Continued_laughing_sounds.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_water_splashing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Laughing_sounds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_More_water_splashing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Continued_laughing_sounds.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of chirping birds", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_chirping_birds.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_chirping_birds.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YoNHCc_izsDE.wav"))
