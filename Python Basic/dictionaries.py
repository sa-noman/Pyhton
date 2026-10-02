"""Dictionaries, nesting, methods, and comprehensions."""
student = {"name": "Noman", "skills": {"python": "learning"}}
student["level"] = "beginner"
print(student.get("name"))
print(student["skills"]["python"])
squares = {n: n * n for n in range(1, 4)}
print(squares)
