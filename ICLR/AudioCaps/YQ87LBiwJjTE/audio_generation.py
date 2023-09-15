
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YQ87LBiwJjTE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Wood stirring in a pot", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Wood_stirring_in_a_pot.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Wood_stirring_in_a_pot.wav")))

TTA(text="Wooden object falling", length=1, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Wooden_object_falling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Wooden_object_falling.wav")))

TTS(text="Let me tell you about this amazing recipe.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Let_me_tell_you_about.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Let_me_tell_you_about.wav")))

TTS(text="First, you need fresh vegetables. Then, add some spices and let it simmer.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_First_you_need_fresh_vegetables.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_First_you_need_fresh_vegetables.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Wood_stirring_in_a_pot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Wooden_object_falling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Let_me_tell_you_about.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_First_you_need_fresh_vegetables.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="Food sizzling in a pan", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Food_sizzling_in_a_pan.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTM(text="Light acoustic guitar music", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Light_acoustic_guitar_music.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Food_sizzling_in_a_pan.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Light_acoustic_guitar_music.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YQ87LBiwJjTE.wav"))
