"""LinkedIn connection-review assistant.

It opens profile URLs for human review and records decisions. It does not
automatically click the Connect button or send invitations.
"""

import argparse
import csv
import json
from pathlib import Path
import webbrowser


def load_profiles(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return [row for row in rows if row.get("profile_url", "").startswith("https://")]


def save_review(log_path: Path, profile_url: str, decision: str) -> None:
    records = []
    if log_path.exists():
        records = json.loads(log_path.read_text(encoding="utf-8"))
    records.append({"profile_url": profile_url, "decision": decision})
    log_path.write_text(json.dumps(records, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--log", type=Path, default=Path("linkedin-review.json"))
    args = parser.parse_args()

    for profile in load_profiles(args.csv_file):
        url = profile["profile_url"]
        print(f"Reviewing: {profile.get('name', '')} {url}")
        webbrowser.open_new_tab(url)
        decision = input("Decision [connect/skip/stop]: ").strip().lower()
        save_review(args.log, url, decision)
        if decision == "stop":
            break


if __name__ == "__main__":
    main()
