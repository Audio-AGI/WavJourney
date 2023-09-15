
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YeRU-rABp8nk/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's a beautiful day, isn't it?", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_day_isnt.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_day_isnt.wav")))

TTS(text="Absolutely. Perfect for a ride.", speaker_id="Male2_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Absolutely_Perfect_for_a_ride.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Absolutely_Perfect_for_a_ride.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_a_beautiful_day_isnt.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Absolutely_Perfect_for_a_ride.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Motorcycle engine idling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Motorcycle_engine_idling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="People talking in a busy setting", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_People_talking_in_a_busy.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Motorcycle_engine_idling.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_People_talking_in_a_busy.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YeRU-rABp8nk.wav"))
