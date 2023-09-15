
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yvigslb0kClE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Move to the left, we don't want to startle them.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Move_to_the_left_we.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Move_to_the_left_we.wav")))

TTS(text="Yes, we need to guide them gently towards the stream.", speaker_id="Male2_En", volume=-18, out_wav=os.path.join(wav_path, "fg_speech_1_Yes_we_need_to_guide.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Yes_we_need_to_guide.wav")))

TTA(text="Shepherd's whistle", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Shepherds_whistle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Shepherds_whistle.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Move_to_the_left_we.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Yes_we_need_to_guide.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Shepherds_whistle.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of a fast running stream", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_fast_running.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Background human chatter sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Background_human_chatter_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Goats bleating, occasional sounds of hooves", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Goats_bleating_occasional_sounds_of.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_fast_running.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Background_human_chatter_sound.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Goats_bleating_occasional_sounds_of.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yvigslb0kClE.wav"))
