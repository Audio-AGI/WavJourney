
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YwNiYSYJXssA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Look at this everyone!", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Look_at_this_everyone.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Look_at_this_everyone.wav")))

TTA(text="Camera plastic clicking sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Camera_plastic_clicking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Camera_plastic_clicking_sound.wav")))

TTA(text="Person whistling sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Person_whistling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Person_whistling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Look_at_this_everyone.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Camera_plastic_clicking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Person_whistling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Crowd of people gasping and talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_gasping_and.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Crowd_of_people_gasping_and.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YwNiYSYJXssA.wav"))
