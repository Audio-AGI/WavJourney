import argparse
import voice_presets

def main():
    # Argument Parsing
    parser = argparse.ArgumentParser(description="Add Voice Preset")
    parser.add_argument("--id", required=True, help="ID of the voice")
    parser.add_argument("--desc", required=True, help="Description of the voice")
    parser.add_argument("--wav-path", required=True, help="Path to the .wav file")
    parser.add_argument("--session-id", required=True, help="session_id, if set to '' then it's system voice presets")
    args = parser.parse_args()

    if args.session_id:
        print(voice_presets.add_session_voice_preset(args.id, args.desc, args.wav_path, args.session_id))
    else:
        print(voice_presets.add_system_voice_preset(args.id, args.desc, args.wav_path))
    
    

if __name__ == "__main__":
    main()
