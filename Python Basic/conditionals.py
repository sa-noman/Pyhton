"""if, elif, else, nested if, conditional expressions, and match/case."""
score = 85
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"
print(grade)
if score >= 50:
    if score >= 80:
        print("High pass")
status = "pass" if score >= 50 else "fail"
print(status)
command = "start"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown")
