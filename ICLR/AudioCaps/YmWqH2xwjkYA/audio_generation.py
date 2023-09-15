
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YmWqH2xwjkYA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="An Infant's laugh", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_An_Infants_laugh.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_An_Infants_laugh.wav")))

TTA(text="A woman's laugh", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_womans_laugh.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_womans_laugh.wav")))

TTA(text="The sound of someone spitting", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_someone_spitting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_someone_spitting.wav")))

TTS(text="That was hilarious, wasn't it? I am so happy today!", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_That_was_hilarious_wasnt_it.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_That_was_hilarious_wasnt_it.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_An_Infants_laugh.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_womans_laugh.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_The_sound_of_someone_spitting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_That_was_hilarious_wasnt_it.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YmWqH2xwjkYA.wav"))
