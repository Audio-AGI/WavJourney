
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YLBe33dw9ezg/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Electronic device buzzes more prominently", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Electronic_device_buzzes_more_prominently.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Electronic_device_buzzes_more_prominently.wav")))

TTS(text="Can you hear me?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Can_you_hear_me.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Can_you_hear_me.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Electronic_device_buzzes_more_prominently.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Can_you_hear_me.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Continuous electronic device buzzing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Continuous_electronic_device_buzzing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTM(text="Soft instrumental music playing", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Soft_instrumental_music_playing.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Continuous_electronic_device_buzzing.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Soft_instrumental_music_playing.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YLBe33dw9ezg.wav"))
