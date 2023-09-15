
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YC5kmOK_l4jc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hey, you're such a cutie. Do you like this toy?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hey_youre_such_a_cutie.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hey_youre_such_a_cutie.wav")))

TTA(text="Infant laughing sound", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Infant_laughing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Infant_laughing_sound.wav")))

TTA(text="Toy squeak sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Toy_squeak_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Toy_squeak_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hey_youre_such_a_cutie.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Infant_laughing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Toy_squeak_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YC5kmOK_l4jc.wav"))
