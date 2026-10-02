"""Function decorators."""
def announce(func):
    def wrapper(*args, **kwargs):
        print("Running function")
        return func(*args, **kwargs)
    return wrapper

@announce
def greet(name):
    return f"Hello, {name}!"

print(greet("Noman"))
