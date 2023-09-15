
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YfrOqlk0Wm5Y/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Just listen to this masterpiece of metallic harmony.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Just_listen_to_this_masterpiece.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Just_listen_to_this_masterpiece.wav")))

TTA(text="Sound of metal clacking", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_metal_clacking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_metal_clacking.wav")))

TTA(text="Sound of metal scraping against a metal surface", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_metal_scraping_against.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_metal_scraping_against.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Just_listen_to_this_masterpiece.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_metal_clacking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_metal_scraping_against.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YfrOqlk0Wm5Y.wav"))
