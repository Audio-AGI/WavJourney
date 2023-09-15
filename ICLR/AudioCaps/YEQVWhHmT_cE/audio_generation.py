
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YEQVWhHmT_cE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Audience clapping", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Audience_clapping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Audience_clapping.wav")))

TTS(text="Ladies and gentlemen, have you ever seen this?", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_have_you.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_have_you.wav")))

TTA(text="Sound of a glass breaking", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_glass_breaking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_glass_breaking.wav")))

TTS(text="Hahaha!", speaker_id="Child_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Hahaha.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hahaha.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Audience_clapping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_have_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_glass_breaking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hahaha.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Restaurant ambiance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Restaurant_ambiance.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Restaurant_ambiance.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YEQVWhHmT_cE.wav"))
