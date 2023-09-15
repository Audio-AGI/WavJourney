
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y3VHpLxtd498/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Crunching and shuffling of gravel", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Crunching_and_shuffling_of_gravel.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Crunching_and_shuffling_of_gravel.wav")))

TTS(text="This is amazing, so many pigeons here.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_amazing_so_many.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_amazing_so_many.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Crunching_and_shuffling_of_gravel.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_amazing_so_many.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous humming sound of a motor", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_humming_sound_of_a.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Pigeons cooing continuously", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Pigeons_cooing_continuously.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_humming_sound_of_a.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Pigeons_cooing_continuously.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y3VHpLxtd498.wav"))
