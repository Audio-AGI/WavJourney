
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YdJYO3RbBabE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Electronic beep", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep.wav")))

TTS(text="Good day, this is your electronic assistant speaking.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Good_day_this_is_your.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Good_day_this_is_your.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Good_day_this_is_your.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YdJYO3RbBabE.wav"))
