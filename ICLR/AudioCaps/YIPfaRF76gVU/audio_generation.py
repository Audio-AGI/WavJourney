
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIPfaRF76gVU/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Emergency vehicle's siren", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Emergency_vehicles_siren.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Emergency_vehicles_siren.wav")))

TTS(text="Get out of the way!", speaker_id="Male1_En", volume=-22, out_wav=os.path.join(wav_path, "fg_speech_0_Get_out_of_the_way.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Get_out_of_the_way.wav")))

TTA(text="Sound of racing vehicle", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_racing_vehicle.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_racing_vehicle.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Emergency_vehicles_siren.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Get_out_of_the_way.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_racing_vehicle.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="City ambiance, traffic sounds", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_City_ambiance_traffic_sounds.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_City_ambiance_traffic_sounds.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIPfaRF76gVU.wav"))
