def parse_age(value: str) -> int:
    age = int(value)
    if not 0 <= age <= 130:
        raise ValueError("Age must be between 0 and 130.")
    return age


if __name__ == "__main__":
    while True:
        try:
            print("Age:", parse_age(input("Enter age: ")))
            break
        except ValueError as exc:
            print("Invalid input:", exc)
