"""Local, enclosing, global, and nonlocal scope."""
value = "global"
def outer():
    value = "enclosing"
    def inner():
        nonlocal value
        value = "changed"
        return value
    return inner()
print(outer())
print(value)
