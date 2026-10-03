import random

def make_secret():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])

def score(secret, guess):
    cows = sum(a == b for a, b in zip(secret, guess))
    bulls = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - cows
    return cows, bulls

if __name__ == "__main__":
    secret = make_secret()
    while True:
        guess = input("4 unique digits: ").strip()
        cows, bulls = score(secret, guess)
        print(f"Cows: {cows}, Bulls: {bulls}")
        if cows == 4:
            break
