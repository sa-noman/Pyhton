from pathlib import Path


def add_note(path: Path, note: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(note.strip() + "\n")


def read_notes(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()]


if __name__ == "__main__":
    notes_file = Path("notes.txt")
    add_note(notes_file, input("Write a note: "))
    print("\nSaved notes:")
    for i, note in enumerate(read_notes(notes_file), 1):
        print(f"{i}. {note}")
