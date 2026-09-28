import secrets
import string


def generate_password(length: int = 16) -> str:
    if length < 8:
        raise ValueError("Use at least 8 characters.")
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print(generate_password())
