
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIdBDl9Wr51A/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="First loud explosion", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_loud_explosion.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_loud_explosion.wav")))

TTS(text="That was quite a blow!", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_That_was_quite_a_blow.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_That_was_quite_a_blow.wav")))

TTA(text="Second loud explosion", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_loud_explosion.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_loud_explosion.wav")))

TTS(text="These explosions are getting closer.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_These_explosions_are_getting_closer.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_These_explosions_are_getting_closer.wav")))

TTA(text="Third loud explosion", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Third_loud_explosion.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Third_loud_explosion.wav")))

TTS(text="We need to get out of here.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_We_need_to_get_out.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_We_need_to_get_out.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_loud_explosion.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_That_was_quite_a_blow.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_loud_explosion.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_These_explosions_are_getting_closer.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Third_loud_explosion.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_We_need_to_get_out.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:6])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Deep booming whooshes", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Deep_booming_whooshes.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Deep_booming_whooshes.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIdBDl9Wr51A.wav"))
