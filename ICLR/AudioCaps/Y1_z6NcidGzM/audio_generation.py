
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y1_z6NcidGzM/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Look at the waves, they're so huge!", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Look_at_the_waves_theyre.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Look_at_the_waves_theyre.wav")))

TTS(text="Uh-huh, this is so much fun!", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Uhhuh_this_is_so_much.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Uhhuh_this_is_so_much.wav")))

TTS(text="Watch out, here comes another wave!", speaker_id="Male1_En", volume=-18, out_wav=os.path.join(wav_path, "fg_speech_2_Watch_out_here_comes_another.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Watch_out_here_comes_another.wav")))

TTA(text="Sound of a closer, louder whistle", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_closer_louder.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_closer_louder.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Look_at_the_waves_theyre.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Uhhuh_this_is_so_much.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Watch_out_here_comes_another.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_closer_louder.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Sound of splashing water", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_splashing_water.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of people screaming in excitement", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_people_screaming_in.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Sound of a distant whistle", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Sound_of_a_distant_whistle.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_splashing_water.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_people_screaming_in.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Sound_of_a_distant_whistle.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y1_z6NcidGzM.wav"))
