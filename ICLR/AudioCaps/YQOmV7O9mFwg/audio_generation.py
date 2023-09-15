
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YQOmV7O9mFwg/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Guess what happened when we were at the park?", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Guess_what_happened_when_we.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Guess_what_happened_when_we.wav")))

TTS(text="We found an adorable puppy! It was so playful and cute.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_We_found_an_adorable_puppy.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_We_found_an_adorable_puppy.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Guess_what_happened_when_we.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_We_found_an_adorable_puppy.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Excited children's laughter", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Excited_childrens_laughter.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[1:2])
bg_audio_offset = sum(fg_audio_lens[:1])
TTA(text="Kids talking", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Kids_talking.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Excited_childrens_laughter.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Kids_talking.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YQOmV7O9mFwg.wav"))
