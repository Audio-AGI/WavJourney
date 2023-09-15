
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yfx4r_KuW6No/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Sweetie, why are you crying?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Sweetie_why_are_you_crying.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Sweetie_why_are_you_crying.wav")))

TTA(text="Child crying sound effect", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Child_crying_sound_effect.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Child_crying_sound_effect.wav")))

TTS(text="I don't know mommy.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_I_dont_know_mommy.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_I_dont_know_mommy.wav")))

TTS(text="It's okay honey. Tell me what's wrong.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_2_Its_okay_honey_Tell_me.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Its_okay_honey_Tell_me.wav")))

TTS(text="I can't find my teddy.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_3_I_cant_find_my_teddy.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_3_I_cant_find_my_teddy.wav")))

TTS(text="Don't worry. We'll find it.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_4_Dont_worry_Well_find_it.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_4_Dont_worry_Well_find_it.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Sweetie_why_are_you_crying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Child_crying_sound_effect.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_I_dont_know_mommy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Its_okay_honey_Tell_me.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_3_I_cant_find_my_teddy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_4_Dont_worry_Well_find_it.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:6])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Buzzing of a home in the daytime", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Buzzing_of_a_home_in.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Buzzing_of_a_home_in.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yfx4r_KuW6No.wav"))
