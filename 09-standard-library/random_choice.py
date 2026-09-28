import random


def choose_random(items: list[str]) -> str:
    if not items:
        raise ValueError("At least one item is required.")
    return random.choice(items)


if __name__ == "__main__":
    items = [x.strip() for x in input("Choices separated by commas: ").split(",") if x.strip()]
    print("Selected:", choose_random(items))
