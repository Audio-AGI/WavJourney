
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YzoctgurhvHE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Some words the man is speaking", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Some_words_the_man_is.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Some_words_the_man_is.wav")))

TTA(text="Plastic clanking sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Plastic_clanking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clanking_sound.wav")))

TTA(text="Door hatch opening", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Door_hatch_opening.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Door_hatch_opening.wav")))

TTA(text="Plastic tumbling sound", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Plastic_tumbling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Plastic_tumbling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Some_words_the_man_is.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Plastic_clanking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Door_hatch_opening.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Plastic_tumbling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Vehicle engine revving", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Vehicle_engine_revving.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Vehicle_engine_revving.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YzoctgurhvHE.wav"))
