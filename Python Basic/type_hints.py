"""Basic type hints."""
def greet(name: str) -> str:
    return f"Hello, {name}!"
def total(values: list[int]) -> int:
    return sum(values)
print(greet("Noman"))
print(total([1, 2, 3]))
