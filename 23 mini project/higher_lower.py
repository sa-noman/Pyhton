import random

def compare(a, b):
    return "higher" if b > a else "lower" if b < a else "equal"

if __name__ == "__main__":
    current = random.randint(1, 100)
    score = 0
    while True:
        print("Current:", current)
        guess = input("Will the next number be higher or lower? ").strip().lower()
        nxt = random.randint(1, 100)
        actual = compare(current, nxt)
        print("Next:", nxt, "->", actual)
        if guess != actual:
            print("Final score:", score)
            break
        score += 1
        current = nxt
