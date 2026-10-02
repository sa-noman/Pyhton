"""Variables, naming, multiple assignment, and globals."""
name = "Noman"
age = 24
x, y, z = 1, 2, 3
a = b = "same"
language = "Python"

def change_global():
    global language
    language = "Python 3"
