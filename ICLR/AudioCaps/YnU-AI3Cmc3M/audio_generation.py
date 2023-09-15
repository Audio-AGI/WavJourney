
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YnU-AI3Cmc3M/audio"
os.makedirs(wav_path, exist_ok=True)


TTA(text="One large bird wing flap", length=5, volume=-25, out_wav=os.path.join(wav_path, "fg_sound_effect_0_One_large_bird_wing_flap.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_One_large_bird_wing_flap.wav")))

TTA(text="A flock of birds flapping their wings", length=5, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_1_A_flock_of_birds_flapping.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_1_A_flock_of_birds_flapping.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_One_large_bird_wing_flap.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_1_A_flock_of_birds_flapping.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:2])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Birds cooing sound, wings flapping", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Birds_cooing_sound_wings_flapping.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Birds_cooing_sound_wings_flapping.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YnU-AI3Cmc3M.wav"))
