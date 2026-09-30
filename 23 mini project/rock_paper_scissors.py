import random

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def result(player, computer):
    if player == computer:
        return "draw"
    return "win" if BEATS[player] == computer else "lose"

def play():
    player = input("rock, paper or scissors: ").strip().lower()
    if player not in CHOICES:
        raise SystemExit("Invalid choice.")
    computer = random.choice(CHOICES)
    print("Computer:", computer)
    print("Result:", result(player, computer))

if __name__ == "__main__":
    play()
