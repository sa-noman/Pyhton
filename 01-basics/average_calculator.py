def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("At least one number is required.")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    raw = input("Enter numbers separated by spaces: ")
    values = [float(x) for x in raw.split()]
    print(f"Average: {average(values):.2f}")
