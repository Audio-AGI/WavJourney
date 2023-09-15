
import os
import sys
import datetime

from APIs import TTM, TTS, TTA, MIX, CAT, COMPUTE_LEN


fg_audio_lens = []
wav_path = "ICLR/AudioCaps/YR91bUbtKrRs/audio"
os.makedirs(wav_path, exist_ok=True)


TTS(text="Hello, how has your day been?", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_0_Hello_how_has_your_day.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_0_Hello_how_has_your_day.wav")))

TTS(text="It's been okay, quite busy though.", speaker_id="Female2_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_1_Its_been_okay_quite_busy.wav"), speaker_npz="v2/de_speaker_3")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_1_Its_been_okay_quite_busy.wav")))

TTA(text="Infant crying sound", length=4, volume=-20, out_wav=os.path.join(wav_path, "fg_sound_effect_0_Infant_crying_sound.wav"))
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_sound_effect_0_Infant_crying_sound.wav")))

TTS(text="Oh dear, it sounds like the baby needs us.", speaker_id="Female1_En", volume=-25, out_wav=os.path.join(wav_path, "fg_speech_2_Oh_dear_it_sounds_like.wav"), speaker_npz="v2/en_speaker_9")
fg_audio_lens.append(COMPUTE_LEN(os.path.join(wav_path, "fg_speech_2_Oh_dear_it_sounds_like.wav")))

fg_audio_wavs = []
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_0_Hello_how_has_your_day.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_1_Its_been_okay_quite_busy.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_sound_effect_0_Infant_crying_sound.wav"))
fg_audio_wavs.append(os.path.join(wav_path, "fg_speech_2_Oh_dear_it_sounds_like.wav"))
CAT(wavs=fg_audio_wavs, out_wav=os.path.join(wav_path, "foreground.wav"))

bg_audio_offsets = []
bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Muted speech sound", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_0_Muted_speech_sound.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_len = sum(fg_audio_lens[0:4])
bg_audio_offset = sum(fg_audio_lens[:0])
TTA(text="Ambient room noise", volume=-35, length=bg_audio_len, out_wav=os.path.join(wav_path, "bg_sound_effect_1_Ambient_room_noise.wav"))
bg_audio_offsets.append(bg_audio_offset)

bg_audio_wavs = []
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_0_Muted_speech_sound.wav"))
bg_audio_wavs.append(os.path.join(wav_path, "bg_sound_effect_1_Ambient_room_noise.wav"))
bg_audio_wav_offset_pairs = list(zip(bg_audio_wavs, bg_audio_offsets))
bg_audio_wav_offset_pairs.append((os.path.join(wav_path, "foreground.wav"), 0))
MIX(wavs=bg_audio_wav_offset_pairs, out_wav=os.path.join(wav_path, "YR91bUbtKrRs.wav"))
