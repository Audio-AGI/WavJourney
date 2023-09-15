
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YzBXoaQ1GVlc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="All right children, settle down.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_All_right_children_settle_down.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_All_right_children_settle_down.wav")))

TTA(text="Children quietening down", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Children_quietening_down.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Children_quietening_down.wav")))

TTS(text="Now, let's continue with our lesson.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Now_lets_continue_with_our.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Now_lets_continue_with_our.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_All_right_children_settle_down.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Children_quietening_down.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Now_lets_continue_with_our.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Children talking and shouting", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Children_talking_and_shouting.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Children_talking_and_shouting.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YzBXoaQ1GVlc.wav"))
