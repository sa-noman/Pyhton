def safe_divide(a: float, b: float) -> tuple[bool, float | str]:
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, "Cannot divide by zero."


if __name__ == "__main__":
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        ok, result = safe_divide(a, b)
        print(result)
    except ValueError:
        print("Please enter valid numbers.")
