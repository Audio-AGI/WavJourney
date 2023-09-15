
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YK8-b0VtNOqA/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a broom sweeping the floor", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_broom_sweeping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_broom_sweeping.wav")))

TTS(text="Anything else you would like to add?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Anything_else_you_would_like.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Anything_else_you_would_like.wav")))

TTS(text="Let's discuss this further.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Lets_discuss_this_further.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Lets_discuss_this_further.wav")))

TTA(text="Distinctive sound of horses neighing", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Distinctive_sound_of_horses_neighing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Distinctive_sound_of_horses_neighing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_broom_sweeping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Anything_else_you_would_like.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Lets_discuss_this_further.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Distinctive_sound_of_horses_neighing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:3])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Ambient chatter of a man conversing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Ambient_chatter_of_a_man.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[1:3])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Ambient chatter of a woman conversing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Ambient_chatter_of_a_woman.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Ambient_chatter_of_a_man.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Ambient_chatter_of_a_woman.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YK8-b0VtNOqA.wav"))
