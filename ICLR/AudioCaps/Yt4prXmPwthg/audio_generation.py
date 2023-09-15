
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yt4prXmPwthg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sewing machine vibrations", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sewing_machine_vibrations.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sewing_machine_vibrations.wav")))

TTS(text="The stitching sounds remind me of simpler times.", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_The_stitching_sounds_remind_me.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_The_stitching_sounds_remind_me.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sewing_machine_vibrations.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_The_stitching_sounds_remind_me.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yt4prXmPwthg.wav"))
