"""Polymorphism through a shared interface."""
class Cat:
    def speak(self): return "meow"
class Dog:
    def speak(self): return "woof"
for animal in (Cat(), Dog()):
    print(animal.speak())
