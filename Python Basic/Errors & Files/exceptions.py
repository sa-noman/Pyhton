"""try, except, else, finally, and raise."""
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    try:
        result = a / b
    except TypeError:
        raise
    else:
        return result
    finally:
        print("Division attempt finished")

print(divide(10, 2))
