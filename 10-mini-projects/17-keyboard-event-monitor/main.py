"""Safe alternative to a keylogger.

This demo captures only text entered directly into this program. It does not
run in the background, hide itself, or monitor system-wide keystrokes.
"""

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
