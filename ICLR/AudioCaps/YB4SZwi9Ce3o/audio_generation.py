
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YB4SZwi9Ce3o/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Just listen to that engine. Smooth as silk.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Just_listen_to_that_engine.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Just_listen_to_that_engine.wav")))

TTA(text="Car engine shifting gears", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Car_engine_shifting_gears.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_shifting_gears.wav")))

TTA(text="Car engine increasing speed", length=4, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Car_engine_increasing_speed.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Car_engine_increasing_speed.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Just_listen_to_that_engine.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Car_engine_shifting_gears.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Car_engine_increasing_speed.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous clicking sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_clicking_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_clicking_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YB4SZwi9Ce3o.wav"))
