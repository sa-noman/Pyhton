from pathlib import Path
import argparse

def record_wav(output, seconds=5, sample_rate=44100):
    import sounddevice as sd
    from scipy.io.wavfile import write
    frames = int(seconds * sample_rate)
    print(f"Recording for {seconds} seconds...")
    audio = sd.rec(frames, samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    write(str(output), sample_rate, audio)
    return Path(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="recording.wav")
    parser.add_argument("--seconds", type=int, default=5)
    args = parser.parse_args()
    print(record_wav(args.output, args.seconds))

if __name__ == "__main__":
    main()
