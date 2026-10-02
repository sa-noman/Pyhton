"""Arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators."""
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
a += 1
print(a == b, a > b)
print(a > 5 and b < 5)
print(a is not b)
print(3 in [1, 2, 3])
print(5 & 3, 5 | 3, 5 ^ 3)
