
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIsUG5SKWNZA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="whispering sound", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_whispering_sound.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_whispering_sound.wav")))

TTA(text="Baby crying sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_sound.wav")))

TTS(text="Call out loudly", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Call_out_loudly.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Call_out_loudly.wav")))

TTS(text="Response over the baby whining noise", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Response_over_the_baby_whining.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Response_over_the_baby_whining.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_whispering_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Baby_crying_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Call_out_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Response_over_the_baby_whining.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Background baby whining sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Background_baby_whining_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Background_baby_whining_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIsUG5SKWNZA.wav"))
