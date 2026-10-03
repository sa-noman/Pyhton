import random

WORDS = ["developer", "algorithm", "computer", "terminal", "package"]

def render(secret, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in secret)

def play(max_misses=6):
    secret = random.choice(WORDS)
    guessed = set()
    misses = 0
    while misses < max_misses:
        print(render(secret, guessed))
        letter = input("Letter: ").strip().lower()[:1]
        if not letter or letter in guessed:
            continue
        guessed.add(letter)
        if letter not in secret:
            misses += 1
        if set(secret) <= guessed:
            print(f"Won: {secret}")
            return True
        print(f"Misses: {misses}/{max_misses}")
    print(f"Lost. Word: {secret}")
    return False

if __name__ == "__main__":
    play()
