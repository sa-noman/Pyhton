def greeting(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = input("Enter your name: ").strip() or "World"
    print(greeting(name))
