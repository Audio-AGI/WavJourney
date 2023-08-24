import os
import argparse
from VoiceParser.model import VoiceParser

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--wav-path', type=str, help="Path of a wav file")
    parser.add_argument('--wav-dir', type=str, help="Directory of wav files")
    parser.add_argument('--out-dir', type=str, help="Directory of output npz files")
    args = parser.parse_args()

    if (args.wav_path is None and args.wav_dir is None) or (args.wav_path is not None and args.wav_dir is not None):
        parser.error("Please provide either '--wav-path' or '--wav-dir', but not both.")

    out_dir = args.out_dir

    model = VoiceParser(device='cpu')

    if args.wav_path is not None:
        model.extract_acoustic_embed(args.wav_path, out_dir)
        print(f'Sucessfully parsed {args.wav_path}')
    else:
        wav_name_list = os.listdir(args.wav_dir)
        for wav_name in wav_name_list:
            wav_path = os.path.join(args.wav_dir, wav_name)
            model.extract_acoustic_embed(wav_path, out_dir)
            print(f'Sucessfully parsed {wav_path}')


if __name__ == '__main__':
    main()
