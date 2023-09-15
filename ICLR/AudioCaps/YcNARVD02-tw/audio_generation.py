
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YcNARVD02-tw/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Did you turn off the water in the bathroom?", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Did_you_turn_off_the.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Did_you_turn_off_the.wav")))

TTS(text="I'm not sure. Let me go check.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Im_not_sure_Let_me.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Im_not_sure_Let_me.wav")))

TTA(text="Sound of footsteps, female", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_footsteps_female.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_footsteps_female.wav")))

TTS(text="Oh no, it was still running.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Oh_no_it_was_still.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Oh_no_it_was_still.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Did_you_turn_off_the.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Im_not_sure_Let_me.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_footsteps_female.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Oh_no_it_was_still.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Subtle sound of indoor environment with faint humming of appliances", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Subtle_sound_of_indoor_environment.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Sound of water running from a tap", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_water_running_from.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Subtle_sound_of_indoor_environment.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_water_running_from.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YcNARVD02-tw.wav"))
