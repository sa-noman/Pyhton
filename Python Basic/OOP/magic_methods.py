"""Special / magic / dunder methods."""
class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title
    def __len__(self):
        return len(self.title)
book = Book("Python")
print(book)
print(len(book))
