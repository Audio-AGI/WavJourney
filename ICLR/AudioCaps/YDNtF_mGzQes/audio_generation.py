
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YDNtF_mGzQes/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Indistinct chatter and whispers", speaker_id="Child_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Indistinct_chatter_and_whispers.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Indistinct_chatter_and_whispers.wav")))

TTS(text="Attention everyone, please listen to the following announcement", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Attention_everyone_please_listen_to.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Attention_everyone_please_listen_to.wav")))

TTA(text="Sound of compressed air releasing", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_compressed_air_releasing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_compressed_air_releasing.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Indistinct_chatter_and_whispers.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Attention_everyone_please_listen_to.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_compressed_air_releasing.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of a large truck engine running", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_large_truck.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_a_large_truck.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YDNtF_mGzQes.wav"))
