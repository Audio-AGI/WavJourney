
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YMTIF_l_8d4Q/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="Sound of a baby crying", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_baby_crying.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_baby_crying.wav")))

TTS(text="There, there, it's okay sweetheart", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_There_there_its_okay_sweetheart.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_There_there_its_okay_sweetheart.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Sound_of_a_baby_crying.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_There_there_its_okay_sweetheart.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_wavs = []
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YMTIF_l_8d4Q.wav"))
