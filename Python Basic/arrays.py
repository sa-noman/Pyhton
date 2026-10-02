"""Typed arrays using Python's standard array module."""
from array import array
numbers = array("i", [10, 20, 30])
numbers.append(40)
print(numbers)
print(numbers[1])
