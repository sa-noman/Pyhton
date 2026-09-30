import random

def generate_target(low=1, high=100, rng=None):
    rng = rng or random
    return rng.randint(low, high)

def compare_guess(guess, target):
    if guess < target:
        return "low"
    if guess > target:
        return "high"
    return "correct"

def play():
    target = generate_target()
    attempts = 0
    while True:
        guess = int(input("Guess a number from 1 to 100: "))
        attempts += 1
        result = compare_guess(guess, target)
        if result == "correct":
            print(f"Correct in {attempts} attempts!")
            return
        print("Too " + result + ".")

if __name__ == "__main__":
    play()
