
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YFXdoNvmrYxo/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, how are you doing?", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_how_are_you_doing.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_how_are_you_doing.wav")))

TTS(text="I'm doing well, thank you.", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Im_doing_well_thank_you.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Im_doing_well_thank_you.wav")))

TTS(text="mmmm", speaker_id="Male2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_mmmm.wav"), speaker_npz="v2/en_speaker_6")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_mmmm.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_how_are_you_doing.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Im_doing_well_thank_you.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_mmmm.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:3])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Birds chirping continuously", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping_continuously.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Birds_chirping_continuously.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YFXdoNvmrYxo.wav"))
