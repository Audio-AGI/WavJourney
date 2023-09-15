
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yir1XTdyt4IY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Loud burst", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Loud_burst.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Loud_burst.wav")))

TTA(text="Metallic ringing sound", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metallic_ringing_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metallic_ringing_sound.wav")))

TTS(text="Did you see the game last night?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Did_you_see_the_game.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Did_you_see_the_game.wav")))

TTS(text="Yeah, it was incredible!", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Yeah_it_was_incredible.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yeah_it_was_incredible.wav")))

TTA(text="Men laughing", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Men_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Men_laughing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Loud_burst.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metallic_ringing_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Did_you_see_the_game.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yeah_it_was_incredible.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Men_laughing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:4])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="General catching up sounds", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_General_catching_up_sounds.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_General_catching_up_sounds.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yir1XTdyt4IY.wav"))
