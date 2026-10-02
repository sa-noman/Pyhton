"""Open, read, write, append, create, and delete files."""
from pathlib import Path
path = Path("example.txt")
path.write_text("First line\n", encoding="utf-8")
with path.open("a", encoding="utf-8") as file:
    file.write("Second line\n")
with path.open("r", encoding="utf-8") as file:
    print(file.read())
created = Path("created_file.txt")
created.touch(exist_ok=True)
path.unlink(missing_ok=True)
created.unlink(missing_ok=True)
