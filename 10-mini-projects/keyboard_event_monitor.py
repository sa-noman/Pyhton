"""Capture text entered directly into this running program."""

def collect_session():
    events = []
    print("Type lines below. Enter /quit to stop.")
    while True:
        text = input("> ")
        if text == "/quit":
            return events
        events.append(text)

if __name__ == "__main__":
    entries = collect_session()
    print("Session input:")
    for entry in entries:
        print(entry)
