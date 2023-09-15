
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YHZ9O6sc7cLA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I could not agree more with the points you've made. It's exceptionally important that we address these issues...", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_could_not_agree_more.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_could_not_agree_more.wav")))

TTS(text="We can make a difference if we continue to prioritize...", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_We_can_make_a_difference.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_We_can_make_a_difference.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_could_not_agree_more.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_We_can_make_a_difference.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Dog barking in distance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Dog_barking_in_distance.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Dog_barking_in_distance.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YHZ9O6sc7cLA.wav"))
