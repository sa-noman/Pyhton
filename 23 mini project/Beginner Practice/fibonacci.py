def fibonacci(count: int) -> list[int]:
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    count = int(input("How many terms? "))
    print(fibonacci(count))
