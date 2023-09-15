
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y8o-Y4QP8LWs/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Alright, let's get started.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Alright_lets_get_started.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Alright_lets_get_started.wav")))

TTA(text="Clattering and thumping of utensils", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clattering_and_thumping_of_utensils.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clattering_and_thumping_of_utensils.wav")))

TTA(text="Metal pinging sound", length=1, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_pinging_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_pinging_sound.wav")))

TTA(text="Whistle sound from afar", length=1, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Whistle_sound_from_afar.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Whistle_sound_from_afar.wav")))

TTS(text="Well, let's see how this goes.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Well_lets_see_how_this.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Well_lets_see_how_this.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Alright_lets_get_started.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clattering_and_thumping_of_utensils.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_pinging_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Whistle_sound_from_afar.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Well_lets_see_how_this.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[4:5])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Continuous sound of liquid splashing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_sound_of_liquid_splashing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_sound_of_liquid_splashing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y8o-Y4QP8LWs.wav"))
