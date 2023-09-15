
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Yj1AiqT5oHZc/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I... uh... it's... um...", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_I_uh_its_um.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_uh_its_um.wav")))

TTA(text="Electronic beep", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep.wav")))

TTS(text="You know... Um... It's... I mean...", speaker_id="Male1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_You_know_Um_Its_I.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_You_know_Um_Its_I.wav")))

TTA(text="Electronic beep", length=5, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_uh_its_um.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Electronic_beep.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_You_know_Um_Its_I.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Electronic_beep.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Random electronic beeping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Random_electronic_beeping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Random_electronic_beeping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Yj1AiqT5oHZc.wav"))
