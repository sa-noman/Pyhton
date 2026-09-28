def analyze_sets(a: set[int], b: set[int]) -> dict:
    return {
        "union": a | b,
        "intersection": a & b,
        "only_a": a - b,
        "only_b": b - a,
    }


if __name__ == "__main__":
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(analyze_sets(a, b))
