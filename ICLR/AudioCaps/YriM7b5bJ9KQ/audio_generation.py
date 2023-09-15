
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YriM7b5bJ9KQ/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A bell clanking", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_bell_clanking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_bell_clanking.wav")))

TTA(text="Laughter of a couple of men", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_couple_of.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_couple_of.wav")))

TTS(text="I can't believe we're finally here.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_I_cant_believe_were_finally.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_cant_believe_were_finally.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_bell_clanking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_couple_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_cant_believe_were_finally.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Distant crowd chatter", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Distant_crowd_chatter.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Distant_crowd_chatter.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YriM7b5bJ9KQ.wav"))
