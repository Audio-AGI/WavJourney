
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y0qbHT34qTZE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="A canon fires", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_A_canon_fires.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_A_canon_fires.wav")))

TTS(text="Cannons ready!", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Cannons_ready.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Cannons_ready.wav")))

TTA(text="Multiple cannons firing", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Multiple_cannons_firing.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Multiple_cannons_firing.wav")))

TTS(text="Good shot!", speaker_id="Male2_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Good_shot.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Good_shot.wav")))

TTA(text="Thunderous sound in the background, setting the ambiance", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Thunderous_sound_in_the_background.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Thunderous_sound_in_the_background.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_A_canon_fires.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Cannons_ready.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Multiple_cannons_firing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Good_shot.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Thunderous_sound_in_the_background.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:5])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Soft sounds of continuous rain splashing on different surfaces", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Soft_sounds_of_continuous_rain.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:5])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Faint sounds of men speaking and conversating", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Faint_sounds_of_men_speaking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Soft_sounds_of_continuous_rain.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Faint_sounds_of_men_speaking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y0qbHT34qTZE.wav"))
