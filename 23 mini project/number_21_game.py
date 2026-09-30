def valid_move(current, next_number):
    return next_number in range(current + 1, min(current + 4, 22))

def computer_move(current):
    target = min(((current // 4) + 1) * 4, 21)
    if target <= current:
        target = min(current + 1, 21)
    return target

def play():
    current = 0
    while current < 21:
        print(f"Current: {current}")
        user = int(input("Choose next number (up to 3 ahead): "))
        if not valid_move(current, user):
            print("Invalid move.")
            continue
        current = user
        if current == 21:
            print("You reached 21!")
            return
        current = computer_move(current)
        print(f"Computer chooses {current}")
        if current == 21:
            print("Computer reached 21.")

if __name__ == "__main__":
    play()
