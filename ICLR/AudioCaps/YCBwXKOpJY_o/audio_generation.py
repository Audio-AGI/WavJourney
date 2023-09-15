
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCBwXKOpJY_o/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, sweetie, how was your day at school today?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_sweetie_how_was_your.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_sweetie_how_was_your.wav")))

TTS(text="It was fun, mom! We learned about dinosaurs today.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_It_was_fun_mom_We.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_It_was_fun_mom_We.wav")))

TTA(text="Sound of a school bus driving off in the background", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_school_bus.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_school_bus.wav")))

TTA(text="Birds chirping in the background", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping_in_the_background.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping_in_the_background.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_sweetie_how_was_your.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_It_was_fun_mom_We.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_school_bus.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Birds_chirping_in_the_background.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCBwXKOpJY_o.wav"))
