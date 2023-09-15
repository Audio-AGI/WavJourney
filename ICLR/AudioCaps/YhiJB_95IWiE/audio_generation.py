
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YhiJB_95IWiE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Clicking sound, like a computer mouse", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_like_a_computer.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_like_a_computer.wav")))

TTS(text="Greetings, I hope today finds you well.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Greetings_I_hope_today_finds.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Greetings_I_hope_today_finds.wav")))

TTA(text="Sanding sound, like sandpaper on wood", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sanding_sound_like_sandpaper_on.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sanding_sound_like_sandpaper_on.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_like_a_computer.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Greetings_I_hope_today_finds.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sanding_sound_like_sandpaper_on.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YhiJB_95IWiE.wav"))
