
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_YS5uKWoB6g/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a crying child", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_crying_child.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_crying_child.wav")))

TTS(text="Can't we do something to quiet him down?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Cant_we_do_something_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Cant_we_do_something_to.wav")))

TTS(text="He's just upset, he'll calm down soon.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Hes_just_upset_hell_calm.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hes_just_upset_hell_calm.wav")))

TTA(text="Car door opening and then closing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Car_door_opening_and_then.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Car_door_opening_and_then.wav")))

TTA(text="Sound of a crying child", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_crying_child.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_crying_child.wav")))

TTS(text="Can't we do something to quiet him down?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Cant_we_do_something_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Cant_we_do_something_to.wav")))

TTS(text="He's just upset, he'll calm down soon.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_3_Hes_just_upset_hell_calm.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_Hes_just_upset_hell_calm.wav")))

TTA(text="Car door opening and then closing", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Car_door_opening_and_then.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Car_door_opening_and_then.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_crying_child.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Cant_we_do_something_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hes_just_upset_hell_calm.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Car_door_opening_and_then.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_crying_child.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Cant_we_do_something_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_Hes_just_upset_hell_calm.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Car_door_opening_and_then.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[4:8])
bg_audio_offset = sum(fg_audio_lens[:4])
TTA(text="Background noise of an urban setting", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Background_noise_of_an_urban.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Background_noise_of_an_urban.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_YS5uKWoB6g.wav"))
