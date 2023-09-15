
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6dLkgq9EKPE/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I warn you, don't try anything funny", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_warn_you_dont_try.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_warn_you_dont_try.wav")))

TTA(text="Sound of a smack", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_smack.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_smack.wav")))

TTA(text="High pitched whistle sound", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_High_pitched_whistle_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_whistle_sound.wav")))

TTS(text="Oh, you'll pay for this!", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Oh_youll_pay_for_this.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Oh_youll_pay_for_this.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_warn_you_dont_try.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_smack.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_High_pitched_whistle_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Oh_youll_pay_for_this.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Engine whining", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Engine_whining.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Engine_whining.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6dLkgq9EKPE.wav"))
