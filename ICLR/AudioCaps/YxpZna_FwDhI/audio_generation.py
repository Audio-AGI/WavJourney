
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YxpZna_FwDhI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Single mouse click", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Single_mouse_click.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Single_mouse_click.wav")))

TTS(text="This is how we turn a simple fabric into a masterpiece.", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_This_is_how_we_turn.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_This_is_how_we_turn.wav")))

TTA(text="Sewing machine stitching fabric", length=7, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Sewing_machine_stitching_fabric.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Sewing_machine_stitching_fabric.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Single_mouse_click.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_This_is_how_we_turn.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Sewing_machine_stitching_fabric.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YxpZna_FwDhI.wav"))
