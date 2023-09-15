
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y6i5eQOpFk_U/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Thumping sound", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Thumping_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Thumping_sound.wav")))

TTS(text="I feel so at peace here. The sound of the water is ethereal.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_I_feel_so_at_peace.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_feel_so_at_peace.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Thumping_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_feel_so_at_peace.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Water running, splashing and gurgling", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Water_running_splashing_and_gurgling.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="People talking in background", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_People_talking_in_background.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Water_running_splashing_and_gurgling.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_People_talking_in_background.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y6i5eQOpFk_U.wav"))
