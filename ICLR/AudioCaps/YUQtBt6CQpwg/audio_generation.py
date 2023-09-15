
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YUQtBt6CQpwg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sewing machine running idle", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sewing_machine_running_idle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sewing_machine_running_idle.wav")))

TTS(text="We're almost done, just a couple more stitches", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Were_almost_done_just_a.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Were_almost_done_just_a.wav")))

TTA(text="Metal ratcheting", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Metal_ratcheting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Metal_ratcheting.wav")))

TTA(text="Metal ratcheting", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Metal_ratcheting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Metal_ratcheting.wav")))

TTA(text="Metal ratcheting", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Metal_ratcheting.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Metal_ratcheting.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sewing_machine_running_idle.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Were_almost_done_just_a.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Metal_ratcheting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Metal_ratcheting.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Metal_ratcheting.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YUQtBt6CQpwg.wav"))
