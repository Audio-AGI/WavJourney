
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yy93cZqNCtks/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of gunshots firing", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_gunshots_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_gunshots_firing.wav")))

TTS(text="There's gunfire! Take cover!", speaker_id="Male1_En", volume=-17, out_wav=os.path.join(wav_path, "fg_speech_0_Theres_gunfire_Take_cover.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Theres_gunfire_Take_cover.wav")))

TTS(text="Roger that, moving into position!", speaker_id="Male2_En", volume=-17, out_wav=os.path.join(wav_path, "fg_speech_1_Roger_that_moving_into_position.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Roger_that_moving_into_position.wav")))

TTA(text="Sound of gunshots firing again", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_gunshots_firing_again.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_gunshots_firing_again.wav")))

TTS(text="We're surrounded! Hold your positions!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_2_Were_surrounded_Hold_your_positions.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Were_surrounded_Hold_your_positions.wav")))

TTA(text="Sound of a dog growling", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_dog_growling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_dog_growling.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_gunshots_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Theres_gunfire_Take_cover.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Roger_that_moving_into_position.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_gunshots_firing_again.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Were_surrounded_Hold_your_positions.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_dog_growling.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of footfalls", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Sound_of_footfalls.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Sound of clicking, like loading a gun", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Sound_of_clicking_like_loading.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Sound_of_footfalls.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Sound_of_clicking_like_loading.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yy93cZqNCtks.wav"))
