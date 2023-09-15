
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YDn3buZWMzwY/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Can you believe this? Just listen to him snore.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Can_you_believe_this_Just.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Can_you_believe_this_Just.wav")))

TTS(text="He is in deep sleep, nothing seems to disturb him.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_He_is_in_deep_sleep.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_He_is_in_deep_sleep.wav")))

TTA(text="Laughing sounds", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Laughing_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Laughing_sounds.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Can_you_believe_this_Just.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_He_is_in_deep_sleep.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Laughing_sounds.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of snoring, steady and rhythmic", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_snoring_steady_and.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_snoring_steady_and.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YDn3buZWMzwY.wav"))
