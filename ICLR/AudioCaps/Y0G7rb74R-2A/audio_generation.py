
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y0G7rb74R-2A/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Thank you everyone, you've been an amazing audience", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Thank_you_everyone_youve_been.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Thank_you_everyone_youve_been.wav")))

TTA(text="Microphone feedback sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Microphone_feedback_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Microphone_feedback_sound.wav")))

TTA(text="Laughter of a crowd", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_crowd.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_crowd.wav")))

TTA(text="Sound of glass clinking", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_glass_clinking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_glass_clinking.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Thank_you_everyone_youve_been.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Microphone_feedback_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Laughter_of_a_crowd.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_glass_clinking.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Ambient sound of a crowd of people laughing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Ambient_sound_of_a_crowd.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Ambient_sound_of_a_crowd.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y0G7rb74R-2A.wav"))
