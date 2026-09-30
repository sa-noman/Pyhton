"""Simple hotword detection with an optional microphone adapter."""

from collections.abc import Iterable
import argparse


def contains_hotword(text: str, hotwords: Iterable[str]) -> str | None:
    normalized = text.casefold()
    for hotword in hotwords:
        word = hotword.strip().casefold()
        if word and word in normalized:
            return hotword
    return None


def microphone_loop(hotwords: list[str]) -> None:
    import speech_recognition as sr

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. Press Ctrl+C to stop.")
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                continue
            detected = contains_hotword(text, hotwords)
            print("Heard:", text)
            if detected:
                print(f"Hotword detected: {detected}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hotword", action="append", default=["computer"])
    parser.add_argument("--text")
    parser.add_argument("--microphone", action="store_true")
    args = parser.parse_args()

    if args.microphone:
        microphone_loop(args.hotword)
        return

    text = args.text if args.text is not None else input("Text: ")
    detected = contains_hotword(text, args.hotword)
    print(f"Detected: {detected}" if detected else "No hotword detected.")


if __name__ == "__main__":
    main()
