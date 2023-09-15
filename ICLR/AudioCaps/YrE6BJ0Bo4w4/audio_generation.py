
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YrE6BJ0Bo4w4/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I'm going to demonstrate something amazing, ready?", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Im_going_to_demonstrate_something.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Im_going_to_demonstrate_something.wav")))

TTA(text="Sound of a water faucet opening and pouring water", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_water_faucet.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_water_faucet.wav")))

TTS(text="Voila, and that's how you do it.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Voila_and_thats_how_you.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Voila_and_thats_how_you.wav")))

TTA(text="Sound of clapping by a single person for a short period in a close area", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_clapping_by_a.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_clapping_by_a.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Im_going_to_demonstrate_something.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_water_faucet.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Voila_and_thats_how_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_clapping_by_a.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Quiet room ambience, woman's light footsteps", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Quiet_room_ambience_womans_light.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Quiet_room_ambience_womans_light.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YrE6BJ0Bo4w4.wav"))
