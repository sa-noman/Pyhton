"""Instagram message automation with dry-run support.

Uses Meta's supported messaging endpoint when --send is explicitly enabled.
"""

from dataclasses import dataclass
import argparse
import os


@dataclass(frozen=True)
class InstagramMessage:
    recipient_id: str
    text: str

    def validate(self) -> None:
        if not self.recipient_id.strip():
            raise ValueError("recipient_id is required")
        if not self.text.strip():
            raise ValueError("message text is required")
        if len(self.text) > 1000:
            raise ValueError("message is too long")


def preview(message: InstagramMessage) -> str:
    message.validate()
    return f"To: {message.recipient_id}\nMessage: {message.text}"


def send_message(ig_user_id: str, message: InstagramMessage, access_token: str) -> dict:
    message.validate()
    if not ig_user_id or not access_token:
        raise ValueError("IG user ID and access token are required")

    import requests

    url = f"https://graph.facebook.com/v21.0/{ig_user_id}/messages"
    response = requests.post(
        url,
        params={"access_token": access_token},
        json={"recipient": {"id": message.recipient_id}, "message": {"text": message.text}},
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("recipient_id")
    parser.add_argument("text")
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()

    job = InstagramMessage(args.recipient_id, args.text)
    print(preview(job))

    if not args.send:
        print("\nDRY RUN: nothing was sent.")
        return

    result = send_message(
        os.environ.get("IG_USER_ID", ""),
        job,
        os.environ.get("META_ACCESS_TOKEN", ""),
    )
    print(result)


if __name__ == "__main__":
    main()
