
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFlk-X0gwjF4/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, I'm beginning my walk in the park.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_Im_beginning_my_walk.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_Im_beginning_my_walk.wav")))

TTA(text="Sound of footsteps on foliage and twigs", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_footsteps_on_foliage.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_footsteps_on_foliage.wav")))

TTA(text="Continued sound of footsteps on foliage and twigs", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Continued_sound_of_footsteps_on.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Continued_sound_of_footsteps_on.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_Im_beginning_my_walk.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_footsteps_on_foliage.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Continued_sound_of_footsteps_on.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Birds chirping in a park's setting", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping_in_a_parks.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping_in_a_parks.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFlk-X0gwjF4.wav"))
