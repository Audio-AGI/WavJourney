
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YemGPabOePzA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Ha ha ha, you're crazy!", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Ha_ha_ha_youre_crazy.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ha_ha_ha_youre_crazy.wav")))

TTA(text="Sound of slowed down laughter", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_slowed_down_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_slowed_down_laughter.wav")))

TTS(text="I know, right! Ha ha ha", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_I_know_right_Ha_ha.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_I_know_right_Ha_ha.wav")))

TTA(text="Sound of slowed down laughter", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_slowed_down_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_slowed_down_laughter.wav")))

TTA(text="Audio distortion, the sound gradually slows down", length=4, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Audio_distortion_the_sound_gradually.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Audio_distortion_the_sound_gradually.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ha_ha_ha_youre_crazy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_slowed_down_laughter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_I_know_right_Ha_ha.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_slowed_down_laughter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Audio_distortion_the_sound_gradually.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YemGPabOePzA.wav"))
