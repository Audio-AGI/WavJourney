
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YP4qd8uodw_M/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="We have to resolve this issue as soon as possible.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_We_have_to_resolve_this.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_We_have_to_resolve_this.wav")))

TTS(text="Yes, I completely agree. Let's discuss our options further.", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_I_completely_agree_Lets.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_I_completely_agree_Lets.wav")))

TTA(text="Light clicks of mouse or keyboard", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Light_clicks_of_mouse_or.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Light_clicks_of_mouse_or.wav")))

TTA(text="Subtle vibrations, like a phone on a wooden desk", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Subtle_vibrations_like_a_phone.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Subtle_vibrations_like_a_phone.wav")))

TTA(text="Digital clicks, similar to a computer processing data", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Digital_clicks_similar_to_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Digital_clicks_similar_to_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_We_have_to_resolve_this.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_I_completely_agree_Lets.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Light_clicks_of_mouse_or.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Subtle_vibrations_like_a_phone.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Digital_clicks_similar_to_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YP4qd8uodw_M.wav"))
