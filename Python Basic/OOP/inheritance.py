"""Inheritance and super concepts."""
class Animal:
    def speak(self):
        return "sound"
class Cat(Animal):
    def speak(self):
        return "meow"
print(Cat().speak())
