"""Encapsulation and private-style attributes."""
class Account:
    def __init__(self, balance=0):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
account = Account(100)
account.deposit(50)
print(account.balance)
