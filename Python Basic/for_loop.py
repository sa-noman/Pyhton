"""for, range, break, continue, pass, and loop else."""
for number in range(1, 6):
    if number == 2:
        continue
    if number == 5:
        break
    print(number)
for _ in range(1):
    pass
for letter in "Python":
    print(letter)
else:
    print("Iteration complete")
