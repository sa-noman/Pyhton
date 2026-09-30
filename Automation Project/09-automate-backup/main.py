"""Create a timestamped ZIP backup and SHA-256 checksum."""

from datetime import datetime
from hashlib import sha256
from pathlib import Path
import argparse
import shutil


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def create_backup(source: Path, destination: Path) -> tuple[Path, str]:
    if not source.exists():
        raise FileNotFoundError(source)
    destination.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_base = destination / f"{source.name}-{timestamp}"
    archive = Path(shutil.make_archive(str(archive_base), "zip", root_dir=source))
    return archive, file_sha256(archive)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    archive, checksum = create_backup(args.source, args.destination)
    print(f"Backup: {archive}")
    print(f"SHA256: {checksum}")


if __name__ == "__main__":
    main()
