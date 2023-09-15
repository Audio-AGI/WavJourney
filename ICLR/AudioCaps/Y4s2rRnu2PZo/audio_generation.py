
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4s2rRnu2PZo/audio"
os.makedirs(wav_path, exist_ok=True)


TTM(text="Action thriller style music stirring anticipation", length=3, volume=-25, out_wav=os.path.join(wav_path, "fg_music_0_Action_thriller_style_music_stirring.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_music_0_Action_thriller_style_music_stirring.wav")))

TTA(text="Banging sound resembling a door being hit", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Banging_sound_resembling_a_door.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Banging_sound_resembling_a_door.wav")))

TTA(text="Whooshing sound resonating as if something passing by quickly", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Whooshing_sound_resonating_as_if.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Whooshing_sound_resonating_as_if.wav")))

TTA(text="Gunshots ringing out, echoing in the night", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Gunshots_ringing_out_echoing_in.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Gunshots_ringing_out_echoing_in.wav")))

TTS(text="Ughh", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Ughh.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Ughh.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_music_0_Action_thriller_style_music_stirring.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Banging_sound_resembling_a_door.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Whooshing_sound_resonating_as_if.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Gunshots_ringing_out_echoing_in.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Ughh.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4s2rRnu2PZo.wav"))
