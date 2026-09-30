import random

FACTS = [
    "Python was first released in 1991.",
    "Octopuses have three hearts.",
    "A day on Venus is longer than its year.",
    "Bananas are berries in botanical classification.",
    "Honey can remain edible for very long periods.",
]

def random_fact(rng=None):
    rng = rng or random
    return rng.choice(FACTS)

if __name__ == "__main__":
    print(random_fact())
