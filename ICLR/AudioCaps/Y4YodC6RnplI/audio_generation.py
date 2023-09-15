
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/Y4YodC6RnplI/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a girl giggling", length=3, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_girl_giggling.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_girl_giggling.wav")))

TTS(text="Haha, you're snoring so loudly!", speaker_id="Female1_En", volume=-15, out_wav=os.path.join(wav_path, "fg_speech_0_Haha_youre_snoring_so_loudly.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Haha_youre_snoring_so_loudly.wav")))

TTA(text="Continuation of girl's laughter", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_girls_laughter.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_girls_laughter.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_girl_giggling.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Haha_youre_snoring_so_loudly.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_Continuation_of_girls_laughter.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[2:3])
bg_audio_offset = sum(fg_audio_lens[:2])
TTA(text="Monotone snoring sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Monotone_snoring_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Monotone_snoring_sound.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "Y4YodC6RnplI.wav"))
