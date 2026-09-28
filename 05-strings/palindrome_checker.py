import re


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def is_palindrome(text: str) -> bool:
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    text = input("Text: ")
    print("Palindrome" if is_palindrome(text) else "Not a palindrome")
