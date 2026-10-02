def list_stats(numbers: list[float]) -> dict:
    if not numbers:
        raise ValueError("List cannot be empty.")
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers),
    }


if __name__ == "__main__":
    values = [float(x) for x in input("Numbers: ").split()]
    print(list_stats(values))
