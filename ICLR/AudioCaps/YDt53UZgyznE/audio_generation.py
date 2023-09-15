
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YDt53UZgyznE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Pretend scream sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Pretend_scream_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Pretend_scream_sound.wav")))

TTA(text="Sound of someone crying", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_someone_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_someone_crying.wav")))

TTS(text="Please, everyone, calm down. It's going to be okay.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Please_everyone_calm_down_Its.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Please_everyone_calm_down_Its.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Pretend_scream_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_someone_crying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Please_everyone_calm_down_Its.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YDt53UZgyznE.wav"))
