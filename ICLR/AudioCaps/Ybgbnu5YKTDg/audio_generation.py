
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Ybgbnu5YKTDg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Attention all units, we have incoming on the south perimeter, take cover", speaker_id="News_Male_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Attention_all_units_we_have.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/news_male_speaker.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Attention_all_units_we_have.wav")))

TTA(text="Intercom beep", length=1, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Intercom_beep.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Intercom_beep.wav")))

TTA(text="Several gunshots firing in a row", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Several_gunshots_firing_in_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Several_gunshots_firing_in_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Attention_all_units_we_have.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Intercom_beep.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Several_gunshots_firing_in_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Helicopter engine running", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Helicopter_engine_running.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Helicopter_engine_running.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Ybgbnu5YKTDg.wav"))
