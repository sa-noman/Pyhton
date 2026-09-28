def analyze_text(text: str) -> dict:
    words = text.split()
    return {
        "characters": len(text),
        "characters_without_spaces": len(text.replace(" ", "")),
        "words": len(words),
        "lines": len(text.splitlines()) or 1,
        "unique_words": len({word.lower().strip(".,!?;:") for word in words}),
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    print(analyze_text(text))
