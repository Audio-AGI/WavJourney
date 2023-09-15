
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YArHiac57pVk/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It was exactly as he said it would be.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_It_was_exactly_as_he.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_It_was_exactly_as_he.wav")))

TTS(text="Indeed, there's no room for doubt.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Indeed_theres_no_room_for.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Indeed_theres_no_room_for.wav")))

TTA(text="First tick of the clock", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_First_tick_of_the_clock.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_First_tick_of_the_clock.wav")))

TTA(text="Second tick of the clock", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Second_tick_of_the_clock.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Second_tick_of_the_clock.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_It_was_exactly_as_he.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Indeed_theres_no_room_for.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_First_tick_of_the_clock.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Second_tick_of_the_clock.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YArHiac57pVk.wav"))
