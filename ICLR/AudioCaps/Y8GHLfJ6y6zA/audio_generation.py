
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y8GHLfJ6y6zA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Whistling a happy tune", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Whistling_a_happy_tune.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Whistling_a_happy_tune.wav")))

TTS(text="The sun is shining brightly, it's going to be a great day", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_The_sun_is_shining_brightly.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_sun_is_shining_brightly.wav")))

TTA(text="Fast typing on a mechanical keyboard", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Fast_typing_on_a_mechanical.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Fast_typing_on_a_mechanical.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Whistling_a_happy_tune.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_sun_is_shining_brightly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Fast_typing_on_a_mechanical.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Occasional faint booms in the distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Occasional_faint_booms_in_the.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Occasional_faint_booms_in_the.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y8GHLfJ6y6zA.wav"))
