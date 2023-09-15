
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YkEP-BwMarf8/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Crumpling paper noise", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Crumpling_paper_noise.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Crumpling_paper_noise.wav")))

TTS(text="You can trash it now, we don't need it anymore.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_You_can_trash_it_now.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_You_can_trash_it_now.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Crumpling_paper_noise.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_You_can_trash_it_now.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YkEP-BwMarf8.wav"))
