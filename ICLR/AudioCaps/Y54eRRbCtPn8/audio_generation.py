
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y54eRRbCtPn8/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This is a brief message from me.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_a_brief_message.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_a_brief_message.wav")))

TTA(text="The sound of slight room echo", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_slight_room.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_slight_room.wav")))

TTA(text="Subtle closing sound of the audio", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Subtle_closing_sound_of_the.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Subtle_closing_sound_of_the.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_a_brief_message.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_slight_room.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Subtle_closing_sound_of_the.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="General atmosphere of a quiet room", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_General_atmosphere_of_a_quiet.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_General_atmosphere_of_a_quiet.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y54eRRbCtPn8.wav"))
