
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y-NrFeH-kBSM/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Gun cocking and firing sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Gun_cocking_and_firing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Gun_cocking_and_firing_sound.wav")))

TTA(text="A piece of metal clanking on a hard surface", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_piece_of_metal_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_piece_of_metal_clanking.wav")))

TTS(text="We aren't going to make it if we don't act now", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_We_arent_going_to_make.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_We_arent_going_to_make.wav")))

TTA(text="Electronic laser sound effect", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Electronic_laser_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Electronic_laser_sound_effect.wav")))

TTA(text="Explosions sound continuing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Explosions_sound_continuing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Explosions_sound_continuing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Gun_cocking_and_firing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_piece_of_metal_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_We_arent_going_to_make.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Electronic_laser_sound_effect.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Explosions_sound_continuing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Gunshots and explosions sound from a distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Gunshots_and_explosions_sound_from.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Gunshots_and_explosions_sound_from.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y-NrFeH-kBSM.wav"))
