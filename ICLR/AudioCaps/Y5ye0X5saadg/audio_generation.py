
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y5ye0X5saadg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Beeping sound of a machine", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Beeping_sound_of_a_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Beeping_sound_of_a_machine.wav")))

TTS(text="We are under attack, requesting immediate backup", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_We_are_under_attack_requesting.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_We_are_under_attack_requesting.wav")))

TTA(text="Multiple blasts and gunshots", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Multiple_blasts_and_gunshots.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Multiple_blasts_and_gunshots.wav")))

TTA(text="More blasts and gunshots", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_More_blasts_and_gunshots.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_More_blasts_and_gunshots.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Beeping_sound_of_a_machine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_We_are_under_attack_requesting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Multiple_blasts_and_gunshots.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_More_blasts_and_gunshots.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Helicopter engine noise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Helicopter_engine_noise.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Helicopter_engine_noise.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y5ye0X5saadg.wav"))
