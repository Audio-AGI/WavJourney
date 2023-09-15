
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y9hxFqltp3xw/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Structure of constant light rustling", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Structure_of_constant_light_rustling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Structure_of_constant_light_rustling.wav")))

TTS(text="Hello, can you hear me? It's been quite a while.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_can_you_hear_me.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_can_you_hear_me.wav")))

TTA(text="Hissing noise", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Hissing_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Hissing_noise.wav")))

TTS(text="Hope it stops soon.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Hope_it_stops_soon.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hope_it_stops_soon.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Structure_of_constant_light_rustling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_can_you_hear_me.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Hissing_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hope_it_stops_soon.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y9hxFqltp3xw.wav"))
