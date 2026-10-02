"""Lists, methods, slicing, and comprehensions."""
numbers = [1, 2, 3]
numbers.append(4)
numbers.extend([5, 6])
numbers.insert(0, 0)
numbers.remove(3)
print(numbers[1:4])
squares = [n * n for n in numbers]
print(squares)
