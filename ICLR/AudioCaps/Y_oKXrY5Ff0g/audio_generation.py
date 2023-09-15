
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y_oKXrY5Ff0g/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I just have to say, this is such an interesting experience for me.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_just_have_to_say.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_just_have_to_say.wav")))

TTA(text="Group of people laughing", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing.wav")))

TTA(text="Plastic crinkling sound", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Plastic_crinkling_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Plastic_crinkling_sound.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_just_have_to_say.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Group_of_people_laughing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Plastic_crinkling_sound.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y_oKXrY5Ff0g.wav"))
