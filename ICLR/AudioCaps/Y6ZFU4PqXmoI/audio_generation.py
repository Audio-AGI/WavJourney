
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6ZFU4PqXmoI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Roaring sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Roaring_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Roaring_sound.wav")))

TTA(text="Cracking noise", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Cracking_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Cracking_noise.wav")))

TTA(text="Metal clinking noise", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Metal_clinking_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Metal_clinking_noise.wav")))

TTS(text="This is interesting. Classic, yet unexpected", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_interesting_Classic_yet.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_interesting_Classic_yet.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Roaring_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Cracking_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Metal_clinking_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_interesting_Classic_yet.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6ZFU4PqXmoI.wav"))
