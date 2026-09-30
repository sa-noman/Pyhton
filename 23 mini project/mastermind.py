import random

def make_code(length=4):
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def score_guess(secret, guess):
    exact = sum(a == b for a, b in zip(secret, guess))
    common = sum(min(secret.count(d), guess.count(d)) for d in set(secret))
    return exact, common - exact

def play():
    secret = make_code()
    while True:
        guess = input("4-digit guess: ").strip()
        if len(guess) != 4 or not guess.isdigit():
            continue
        exact, misplaced = score_guess(secret, guess)
        print(f"Exact: {exact}, misplaced: {misplaced}")
        if exact == 4:
            return

if __name__ == "__main__":
    play()
