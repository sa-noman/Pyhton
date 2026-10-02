"""Classes, objects, __init__, self, methods, and properties."""
class Person:
    species = "Human"
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def greet(self):
        return f"Hello, I am {self.name}."

person = Person("Noman")
print(person.greet())
