
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YJQz40TkjymY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Fast typing starts", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Fast_typing_starts.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Fast_typing_starts.wav")))

TTA(text="Pauses and slower typing, spacebar sounds", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Pauses_and_slower_typing_spacebar.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Pauses_and_slower_typing_spacebar.wav")))

TTA(text="Resuming with a steady pace of typing sounds", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Resuming_with_a_steady_pace.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Resuming_with_a_steady_pace.wav")))

TTA(text="Wrapping up with slower typing and a definitive enter key press", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Wrapping_up_with_slower_typing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Wrapping_up_with_slower_typing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Fast_typing_starts.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Pauses_and_slower_typing_spacebar.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Resuming_with_a_steady_pace.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Wrapping_up_with_slower_typing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Subtle room ambiance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Subtle_room_ambiance.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Subtle_room_ambiance.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YJQz40TkjymY.wav"))
