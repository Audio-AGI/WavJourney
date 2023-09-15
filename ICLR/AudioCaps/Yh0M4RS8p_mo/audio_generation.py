
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yh0M4RS8p_mo/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Audio static", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Audio_static.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Audio_static.wav")))

TTS(text="Haha! Wonderful.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Haha_Wonderful.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Haha_Wonderful.wav")))

TTA(text="Electronic device motor sliding", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Electronic_device_motor_sliding.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Electronic_device_motor_sliding.wav")))

TTA(text="Infant crying", length=3, volume=-16, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Infant_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Infant_crying.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Audio_static.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Haha_Wonderful.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Electronic_device_motor_sliding.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Infant_crying.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yh0M4RS8p_mo.wav"))
