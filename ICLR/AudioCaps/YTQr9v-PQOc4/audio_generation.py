
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YTQr9v-PQOc4/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Clicking sound of mouse buttons", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_of_mouse_buttons.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_of_mouse_buttons.wav")))

TTA(text="Sound of a person sneezing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_person_sneezing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_person_sneezing.wav")))

TTS(text="Hahaha", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hahaha.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hahaha.wav")))

TTA(text="Sound of laughter, a man is laughing", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_laughter_a_man.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_laughter_a_man.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clicking_sound_of_mouse_buttons.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_person_sneezing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hahaha.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_laughter_a_man.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YTQr9v-PQOc4.wav"))
