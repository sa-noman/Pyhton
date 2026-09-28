import json
from pathlib import Path


def add_expense(expenses: list[dict], title: str, amount: float, category: str) -> None:
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    expenses.append({"title": title, "amount": amount, "category": category})


def total_expenses(expenses: list[dict]) -> float:
    return sum(float(item["amount"]) for item in expenses)


def save_expenses(expenses: list[dict], path: Path) -> None:
    path.write_text(json.dumps(expenses, indent=2), encoding="utf-8")


def load_expenses(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    data_file = Path("expenses.json")
    expenses = load_expenses(data_file)
    title = input("Expense title: ").strip()
    amount = float(input("Amount: "))
    category = input("Category: ").strip() or "Other"
    add_expense(expenses, title, amount, category)
    save_expenses(expenses, data_file)
    print(f"Total expenses: {total_expenses(expenses):.2f}")
