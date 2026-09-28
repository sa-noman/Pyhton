import random


def play() -> None:
    target = random.randint(1, 100)
    attempts = 0
    print("Guess a number from 1 to 100.")
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < target:
            print("Too low.")
        elif guess > target:
            print("Too high.")
        else:
            print(f"Correct in {attempts} attempts!")
            break


if __name__ == "__main__":
    play()
