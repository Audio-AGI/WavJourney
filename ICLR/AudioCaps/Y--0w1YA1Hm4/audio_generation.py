
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y--0w1YA1Hm4/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Can you believe we just did that?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Can_you_believe_we_just.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Can_you_believe_we_just.wav")))

TTS(text="No, I never imagined it!", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_No_I_never_imagined_it.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_No_I_never_imagined_it.wav")))

TTA(text="Laughter of man and woman", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_man_and_woman.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_man_and_woman.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Can_you_believe_we_just.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_No_I_never_imagined_it.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Laughter_of_man_and_woman.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of a vehicle driving", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_vehicle_driving.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_vehicle_driving.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y--0w1YA1Hm4.wav"))
