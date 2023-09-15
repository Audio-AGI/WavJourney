
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YbUTOsLXYyxg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Our future depends on today's actions.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Our_future_depends_on_todays.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Our_future_depends_on_todays.wav")))

TTS(text="I completely agree, we need to take our commitments seriously.", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_I_completely_agree_we_need.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_I_completely_agree_we_need.wav")))

TTA(text="Group of people laughing loudly", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing_loudly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing_loudly.wav")))

TTS(text="We need to work together to make a difference.", speaker_id="Old_Man_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_We_need_to_work_together.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/elder_morgen.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_We_need_to_work_together.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Our_future_depends_on_todays.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_I_completely_agree_we_need.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_We_need_to_work_together.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Man speaking in the background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Man_speaking_in_the_background.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Man_speaking_in_the_background.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YbUTOsLXYyxg.wav"))
