from pathlib import Path


def file_word_count(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


if __name__ == "__main__":
    path = Path(input("File path: ").strip())
    print(file_word_count(path))
