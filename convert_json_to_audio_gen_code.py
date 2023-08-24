import argparse
import os
import json5
from pathlib import Path
from code_generator import AudioCodeGenerator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", help="Path to the json script file")
    parser.add_argument("--character-to-voice-map", help="Path to the character-to-voice mapping CSV file")
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Path of all the output wav files to be created by the generated code, default: current path"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.script):
        print(f"File {args.script} does not exist.")
        return

    output_path = Path(args.path)
    audio_code_generator = AudioCodeGenerator()
    code = audio_code_generator.parse_and_generate(args.script, args.character_to_voice_map, output_path)
    print(code)

if __name__ == "__main__":
    main()
