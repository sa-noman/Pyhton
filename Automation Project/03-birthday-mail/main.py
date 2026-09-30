"""Send a birthday greeting through SMTP. Dry-run is the default."""

from email.message import EmailMessage
import argparse
import os
import smtplib
import ssl


def build_mail(recipient: str, name: str, sender: str) -> EmailMessage:
    if "@" not in recipient or "@" not in sender:
        raise ValueError("valid sender and recipient emails are required")
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = f"Happy Birthday, {name}!"
    msg.set_content(
        f"Hi {name},\n\nHappy Birthday! Wishing you a joyful day and a great year ahead.\n"
    )
    return msg


def send_mail(message: EmailMessage, host: str, port: int, password: str) -> None:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(message["From"], password)
        smtp.send_message(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("recipient")
    parser.add_argument("name")
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()

    sender = os.environ.get("SMTP_USER", "sender@example.com")
    message = build_mail(args.recipient, args.name, sender)
    print(message)

    if not args.send:
        print("DRY RUN: email not sent.")
        return

    send_mail(
        message,
        os.environ.get("SMTP_HOST", "smtp.gmail.com"),
        int(os.environ.get("SMTP_PORT", "465")),
        os.environ["SMTP_PASSWORD"],
    )


if __name__ == "__main__":
    main()
