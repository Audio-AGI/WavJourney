
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6aWnK1GyeJY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Baby crying", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Baby_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying.wav")))

TTA(text="Sneezing sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sneezing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sneezing_sound.wav")))

TTA(text="Baby crying", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Baby_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Baby_crying.wav")))

TTS(text="Oh dear, it's okay.", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Oh_dear_its_okay.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Oh_dear_its_okay.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sneezing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Baby_crying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Oh_dear_its_okay.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6aWnK1GyeJY.wav"))
