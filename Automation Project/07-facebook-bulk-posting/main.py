"""Post one message to multiple Facebook Pages you manage.

Dry-run by default. Real posting requires --send and a Page access token.
"""

from dataclasses import dataclass
import argparse
import json
from pathlib import Path
import os
import time


@dataclass(frozen=True)
class PagePost:
    page_id: str
    message: str


def load_jobs(path: Path) -> list[PagePost]:
    data = json.loads(path.read_text(encoding="utf-8"))
    jobs = [PagePost(str(item["page_id"]), str(item["message"])) for item in data]
    if len(jobs) > 10:
        raise ValueError("This demo limits a run to 10 Page posts.")
    return jobs


def publish(job: PagePost, token: str) -> dict:
    import requests

    response = requests.post(
        f"https://graph.facebook.com/v21.0/{job.page_id}/feed",
        data={"message": job.message, "access_token": token},
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("jobs", type=Path)
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--delay", type=float, default=2.0)
    args = parser.parse_args()

    jobs = load_jobs(args.jobs)
    for job in jobs:
        print(f"Page {job.page_id}: {job.message}")
        if args.send:
            print(publish(job, os.environ["META_ACCESS_TOKEN"]))
            time.sleep(max(args.delay, 1.0))

    if not args.send:
        print("DRY RUN: no posts were created.")


if __name__ == "__main__":
    main()
