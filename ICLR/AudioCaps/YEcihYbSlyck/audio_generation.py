
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YEcihYbSlyck/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Electronic beep repeatedly sounds", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep_repeatedly_sounds.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep_repeatedly_sounds.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep_repeatedly_sounds.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Train horns honking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Train_horns_honking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Wind blowing into microphone", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing_into_microphone.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Group of people talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_2_Group_of_people_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:1])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Vehicle engine running idle", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_3_Vehicle_engine_running_idle.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Train_horns_honking.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Wind_blowing_into_microphone.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_2_Group_of_people_talking.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_3_Vehicle_engine_running_idle.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YEcihYbSlyck.wav"))
