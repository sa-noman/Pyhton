import re
from collections import Counter


def word_frequency(text: str) -> Counter:
    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    return Counter(words)


if __name__ == "__main__":
    text = input("Text: ")
    for word, count in word_frequency(text).most_common():
        print(f"{word}: {count}")
