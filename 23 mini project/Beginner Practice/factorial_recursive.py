def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    number = int(input("Number: "))
    print(factorial(number))
