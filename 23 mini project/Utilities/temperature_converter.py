def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    celsius = float(input("Celsius: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.1f}")
