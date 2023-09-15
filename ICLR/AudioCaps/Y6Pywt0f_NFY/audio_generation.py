
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6Pywt0f_NFY/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Constant stream of water running", length=10, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Constant_stream_of_water_running.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Constant_stream_of_water_running.wav")))

TTA(text="Water gushing out", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Water_gushing_out.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Water_gushing_out.wav")))

TTA(text="Water hitting the surface", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Water_hitting_the_surface.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Water_hitting_the_surface.wav")))

TTA(text="Soothing sound of flowing water", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Soothing_sound_of_flowing_water.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Soothing_sound_of_flowing_water.wav")))

TTA(text="Water splashes", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Water_splashes.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Water_splashes.wav")))

TTA(text="Gentle stream of water", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_5_Gentle_stream_of_water.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_5_Gentle_stream_of_water.wav")))

TTA(text="Last few drops of water", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_6_Last_few_drops_of_water.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_6_Last_few_drops_of_water.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Constant_stream_of_water_running.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Water_gushing_out.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Water_hitting_the_surface.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Soothing_sound_of_flowing_water.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Water_splashes.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_5_Gentle_stream_of_water.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_6_Last_few_drops_of_water.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:7])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Echoing drop of water", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Echoing_drop_of_water.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Echoing_drop_of_water.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6Pywt0f_NFY.wav"))
