from hashlib import sha256
from pathlib import Path

def file_hash(path):
    digest = sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def identical(path_a, path_b):
    a, b = Path(path_a), Path(path_b)
    return a.stat().st_size == b.stat().st_size and file_hash(a) == file_hash(b)

if __name__ == "__main__":
    first = input("First PDF: ")
    second = input("Second PDF: ")
    print("Identical" if identical(first, second) else "Different")
