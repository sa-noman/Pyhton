"""Send personalized emails from CSV. Dry-run by default."""

from email.message import EmailMessage
from pathlib import Path
import argparse
import csv
import os
import smtplib
import ssl


def load_contacts(path: Path, limit: int = 20) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        contacts = list(csv.DictReader(handle))
    if len(contacts) > limit:
        raise ValueError(f"This demo allows at most {limit} recipients per run.")
    return contacts


def build_message(sender: str, row: dict[str, str], template: str) -> EmailMessage:
    recipient = row["email"].strip()
    name = row.get("name", "there").strip() or "there"
    if "@" not in recipient:
        raise ValueError(f"Invalid email: {recipient}")
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = row.get("subject", "Hello")
    msg.set_content(template.format(name=name))
    return msg


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("contacts", type=Path)
    parser.add_argument("--template", default="Hi {name},\n\nThis is an automated message.")
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()

    sender = os.environ.get("SMTP_USER", "sender@example.com")
    messages = [build_message(sender, row, args.template) for row in load_contacts(args.contacts)]

    if not args.send:
        for msg in messages:
            print(f"DRY RUN -> {msg['To']}: {msg['Subject']}")
        return

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        os.environ.get("SMTP_HOST", "smtp.gmail.com"),
        int(os.environ.get("SMTP_PORT", "465")),
        context=context,
    ) as smtp:
        smtp.login(sender, os.environ["SMTP_PASSWORD"])
        for msg in messages:
            smtp.send_message(msg)


if __name__ == "__main__":
    main()
