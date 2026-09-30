"""Create a birthday post and optionally publish it to a Facebook Page you manage."""

import argparse
import os


def build_birthday_message(name: str, custom_note: str = "") -> str:
    name = name.strip()
    if not name:
        raise ValueError("name is required")
    base = f"Happy Birthday, {name}! Wishing you a wonderful year ahead."
    return f"{base} {custom_note.strip()}".strip()


def publish_to_page(page_id: str, message: str, access_token: str) -> dict:
    if not page_id or not access_token:
        raise ValueError("page ID and access token are required")

    import requests

    response = requests.post(
        f"https://graph.facebook.com/v21.0/{page_id}/feed",
        data={"message": message, "access_token": access_token},
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--note", default="")
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()

    message = build_birthday_message(args.name, args.note)
    print(message)

    if not args.send:
        print("\nDRY RUN: no Facebook post was created.")
        return

    result = publish_to_page(
        os.environ.get("FACEBOOK_PAGE_ID", ""),
        message,
        os.environ.get("META_ACCESS_TOKEN", ""),
    )
    print(result)


if __name__ == "__main__":
    main()
