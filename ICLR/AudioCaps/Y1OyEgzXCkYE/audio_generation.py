
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1OyEgzXCkYE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Ladies and gentlemen, I appreciate you all for being here today. The future is bright for us, and together we will make a change. Thank you.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_I_appreciate.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_I_appreciate.wav")))

TTA(text="Casual clapping sound for 3 seconds", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Casual_clapping_sound_for_.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Casual_clapping_sound_for_.wav")))

TTM(text="Piano outro music", length=6, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Piano_outro_music.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Piano_outro_music.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ladies_and_gentlemen_I_appreciate.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Casual_clapping_sound_for_.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Piano_outro_music.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1OyEgzXCkYE.wav"))
