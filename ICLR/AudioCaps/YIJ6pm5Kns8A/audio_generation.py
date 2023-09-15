
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YIJ6pm5Kns8A/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="I think we can all agree, this has been quite the eventful day", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_I_think_we_can_all.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_I_think_we_can_all.wav")))

TTA(text="Phone chimes softly", length=1, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Phone_chimes_softly.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Phone_chimes_softly.wav")))

TTA(text="Comedic, exaggerated burp sound", length=1, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Comedic_exaggerated_burp_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Comedic_exaggerated_burp_sound.wav")))

TTA(text="Loud, contagious laughter", length=2, volume=-15, out_wav=os.path.join(wav_path, "fg_sound_effect_2_Loud_contagious_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_2_Loud_contagious_laughter.wav")))

TTA(text="Warm, comforting applause", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_3_Warm_comforting_applause.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_3_Warm_comforting_applause.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_I_think_we_can_all.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Phone_chimes_softly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Comedic_exaggerated_burp_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_2_Loud_contagious_laughter.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_3_Warm_comforting_applause.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YIJ6pm5Kns8A.wav"))
