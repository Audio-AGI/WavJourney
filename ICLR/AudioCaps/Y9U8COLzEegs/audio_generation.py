
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9U8COLzEegs/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Electronic beeping sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Electronic_beeping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beeping_sound.wav")))

TTS(text="Here's a little about our latest technology project.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Heres_a_little_about_our.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Heres_a_little_about_our.wav")))

TTS(text="With this, we can enhance our productivity and efficiency.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_With_this_we_can_enhance.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_With_this_we_can_enhance.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beeping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Heres_a_little_about_our.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_With_this_we_can_enhance.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of water pouring", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_pouring.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_water_pouring.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9U8COLzEegs.wav"))
