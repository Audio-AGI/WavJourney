
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YC8kR19NvynA/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Sometimes, life might throw challenges at us. Unseen events, unforeseen circumstances. But remember, every adversity offers an equal seed of advantage. Through tribulations we often find our greatest strengths. We may be hammered down, but we are never defeated. Always, remember that.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Sometimes_life_might_throw_challenges.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Sometimes_life_might_throw_challenges.wav")))

TTA(text="Clock ticking sound", length=3, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking_sound.wav")))

TTA(text="Sound of a heart beating", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_heart_beating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_heart_beating.wav")))

TTS(text="It's welcoming the storms of life, knowing that they will pass. And once they do, we emerge stronger, wiser, better.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Its_welcoming_the_storms_of.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Its_welcoming_the_storms_of.wav")))

TTA(text="Sound of rain", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_rain.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_rain.wav")))

TTA(text="Sound of thunder", length=1, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Sound_of_thunder.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_thunder.wav")))

TTA(text="Sound of a heart beating", length=3, volume=-22, out_wav=os.path.join(wav_path, "fg_sound_effect_4_Sound_of_a_heart_beating.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_4_Sound_of_a_heart_beating.wav")))

TTS(text="To become the best version of ourselves, we need to face our fears head-on. And if you take one thing from this monologue, let it be this - never stop believing in yourself.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_2_To_become_the_best_version.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_To_become_the_best_version.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Sometimes_life_might_throw_challenges.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Clock_ticking_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_a_heart_beating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Its_welcoming_the_storms_of.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_rain.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Sound_of_thunder.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_4_Sound_of_a_heart_beating.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_To_become_the_best_version.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[1:8])
bg_audio_offset = sum(fg_audio_lens[:1])
TTM(text="Peaceful piano melody", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_music_0_Peaceful_piano_melody.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_music_0_Peaceful_piano_melody.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YC8kR19NvynA.wav"))
