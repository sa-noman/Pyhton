"""while, break, continue, and loop else."""
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
    if count == 4:
        break
    print(count)
else:
    print("Loop completed normally")
