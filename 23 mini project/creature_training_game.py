from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    level: int = 1
    xp: int = 0

    def train(self, points=10):
        self.xp += points
        while self.xp >= self.level * 20:
            self.xp -= self.level * 20
            self.level += 1

def main():
    creature = Creature(input("Creature name: ").strip() or "Spark")
    for _ in range(3):
        creature.train(15)
        print(creature)

if __name__ == "__main__":
    main()
