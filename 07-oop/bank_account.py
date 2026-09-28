class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Student", 1000)
    account.deposit(500)
    account.withdraw(250)
    print(account.balance)
