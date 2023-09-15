
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yq1ivQ_2fddk/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's a beautiful day, isn't it?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_day_isnt.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_day_isnt.wav")))

TTA(text="Footsteps approaching", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Footsteps_approaching.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_approaching.wav")))

TTS(text="Indeed, couldn't agree more.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Indeed_couldnt_agree_more.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Indeed_couldnt_agree_more.wav")))

TTA(text="More footsteps approaching", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_More_footsteps_approaching.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_More_footsteps_approaching.wav")))

TTS(text="What are you guys talking about?", speaker_id="Old_Man_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_What_are_you_guys_talking.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/elder_morgen.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_What_are_you_guys_talking.wav")))

TTS(text="Just how lovely this day is.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_3_Just_how_lovely_this_day.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_Just_how_lovely_this_day.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_day_isnt.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Footsteps_approaching.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Indeed_couldnt_agree_more.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_More_footsteps_approaching.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_What_are_you_guys_talking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_Just_how_lovely_this_day.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:6])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="City street ambiance, cars passing by", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_City_street_ambiance_cars_passing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_City_street_ambiance_cars_passing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yq1ivQ_2fddk.wav"))
