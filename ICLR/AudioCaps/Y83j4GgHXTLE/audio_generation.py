
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y83j4GgHXTLE/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Children screaming in delight", length=3, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Children_screaming_in_delight.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Children_screaming_in_delight.wav")))

TTA(text="A man laughing heartily", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_man_laughing_heartily.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_man_laughing_heartily.wav")))

TTS(text="Be quiet, they'll hear us.", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Be_quiet_theyll_hear_us.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Be_quiet_theyll_hear_us.wav")))

TTS(text="I'm not scared, they're just playing.", speaker_id="Child_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_1_Im_not_scared_theyre_just.wav"), speaker_npz="/home/lxb/Disk_SSD/WavJourney/data/voice_presets/npz/child_boy.npz")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Im_not_scared_theyre_just.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Children_screaming_in_delight.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_man_laughing_heartily.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Be_quiet_theyll_hear_us.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Im_not_scared_theyre_just.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y83j4GgHXTLE.wav"))
