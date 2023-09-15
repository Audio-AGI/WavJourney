
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y7P6lcyeDKNI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of dirt being shuffled", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_dirt_being_shuffled.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_dirt_being_shuffled.wav")))

TTA(text="Sound of gears cranking", length=3, volume=-18, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sound_of_gears_cranking.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_gears_cranking.wav")))

TTA(text="Sound of a branch snapping", length=1, volume=-17, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_branch_snapping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_branch_snapping.wav")))

TTS(text="Look what you've done now", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Look_what_youve_done_now.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Look_what_youve_done_now.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_dirt_being_shuffled.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sound_of_gears_cranking.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Sound_of_a_branch_snapping.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Look_what_youve_done_now.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y7P6lcyeDKNI.wav"))
