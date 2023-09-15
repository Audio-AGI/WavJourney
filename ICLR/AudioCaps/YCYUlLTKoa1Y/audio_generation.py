
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YCYUlLTKoa1Y/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="This sewing machine will stitch slowly for about ten seconds.", speaker_id="Female1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_This_sewing_machine_will_stitch.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_sewing_machine_will_stitch.wav")))

TTA(text="Sound of a sewing machine slowly stitching", length=10, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_sewing_machine.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_sewing_machine.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_sewing_machine_will_stitch.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_sewing_machine.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YCYUlLTKoa1Y.wav"))
