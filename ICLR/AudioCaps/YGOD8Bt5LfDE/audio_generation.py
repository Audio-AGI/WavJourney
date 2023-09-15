
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YGOD8Bt5LfDE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Laughter of children", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_children.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_children.wav")))

TTS(text="You kids are just too entertaining!", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_You_kids_are_just_too.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_You_kids_are_just_too.wav")))

TTS(text="We just love to make you laugh, Dad!", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_We_just_love_to_make.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_We_just_love_to_make.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_children.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_You_kids_are_just_too.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_We_just_love_to_make.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous humming and vibrating noise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_humming_and_vibrating_noise.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_humming_and_vibrating_noise.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YGOD8Bt5LfDE.wav"))
