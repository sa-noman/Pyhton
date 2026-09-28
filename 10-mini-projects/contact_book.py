def add_contact(contacts: dict[str, str], name: str, phone: str) -> None:
    contacts[name.strip()] = phone.strip()


def find_contact(contacts: dict[str, str], name: str) -> str | None:
    return contacts.get(name.strip())


if __name__ == "__main__":
    contacts: dict[str, str] = {}
    add_contact(contacts, "Alice", "0123456789")
    print(find_contact(contacts, "Alice"))
