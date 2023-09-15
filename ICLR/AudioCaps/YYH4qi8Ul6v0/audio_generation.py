
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YYH4qi8Ul6v0/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="It's alright, don't cry little one.", speaker_id="Male1_En", volume=-20, out_wav=os.path.join(wav_path, "fg_speech_0_Its_alright_dont_cry_little.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Its_alright_dont_cry_little.wav")))

TTA(text="The sound of an infant crying", length=2, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_an_infant.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_an_infant.wav")))

TTS(text="Hmmm hmm hmm...", speaker_id="Male1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_1_Hmmm_hmm_hmm.wav"), speaker_npz="v2/en_speaker_1")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Hmmm_hmm_hmm.wav")))

TTA(text="Comforting humming sound made by a man", length=2, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Comforting_humming_sound_made_by.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Comforting_humming_sound_made_by.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Its_alright_dont_cry_little.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_The_sound_of_an_infant.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Hmmm_hmm_hmm.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Comforting_humming_sound_made_by.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[3:4])
bg_audio_offset = sum(fg_audio_lens[:3])
TTA(text="A calm and comfortable room ambiance", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_A_calm_and_comfortable_room.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_A_calm_and_comfortable_room.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YYH4qi8Ul6v0.wav"))
