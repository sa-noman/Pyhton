import random

WORDS = ["python", "variable", "function", "program", "object"]

def masked_word(secret, guessed):
    return "".join(ch if ch in guessed else "_" for ch in secret)

def play(words=None):
    secret = random.choice(words or WORDS)
    guessed = set()
    while True:
        print(masked_word(secret, guessed))
        letter = input("Guess one letter: ").strip().lower()[:1]
        if not letter:
            continue
        guessed.add(letter)
        if all(ch in guessed for ch in secret):
            print(f"You found it: {secret}")
            return secret

if __name__ == "__main__":
    play()
