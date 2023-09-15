
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y2a6GNu6uCDE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of microphone getting switched on", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_microphone_getting_switched.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_microphone_getting_switched.wav")))

TTS(text="Good afternoon everyone, thank you for being here.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Good_afternoon_everyone_thank_you.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Good_afternoon_everyone_thank_you.wav")))

TTA(text="Sound of microphone getting switched off", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_microphone_getting_switched.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_microphone_getting_switched.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_microphone_getting_switched.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Good_afternoon_everyone_thank_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_microphone_getting_switched.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y2a6GNu6uCDE.wav"))
