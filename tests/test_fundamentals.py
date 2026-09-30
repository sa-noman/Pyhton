import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


calculator = load("calculator", "01-basics/calculator.py")
temperature = load("temperature", "01-basics/temperature_converter.py")
grades = load("grades", "02-control-flow/grade_checker.py")
leap = load("leap", "02-control-flow/leap_year.py")
stats = load("stats", "03-data-structures/list_statistics.py")
words = load("words", "03-data-structures/word_frequency.py")
prime = load("prime", "04-functions/prime_checker.py")
fib = load("fib", "04-functions/fibonacci.py")
factorial = load("factorial", "04-functions/factorial_recursive.py")
palindrome = load("palindrome", "05-strings/palindrome_checker.py")
files = load("files", "06-file-handling/file_word_counter.py")
bank = load("bank", "07-oop/bank_account.py")
expenses = load("expenses", "23 mini project/expense_tracker.py")


class FundamentalTests(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calculator.calculate(4, 2, "*"), 8)
        with self.assertRaises(ValueError):
            calculator.calculate(1, 0, "/")

    def test_temperature(self):
        self.assertAlmostEqual(temperature.celsius_to_fahrenheit(0), 32)

    def test_grade(self):
        self.assertEqual(grades.letter_grade(85), "A+")

    def test_leap_year(self):
        self.assertTrue(leap.is_leap_year(2024))
        self.assertFalse(leap.is_leap_year(2100))

    def test_list_stats(self):
        self.assertEqual(stats.list_stats([1, 2, 3])["average"], 2)

    def test_word_frequency(self):
        self.assertEqual(words.word_frequency("AI ai Python")["ai"], 2)

    def test_prime(self):
        self.assertTrue(prime.is_prime(29))
        self.assertFalse(prime.is_prime(21))

    def test_fibonacci(self):
        self.assertEqual(fib.fibonacci(6), [0, 1, 1, 2, 3, 5])

    def test_factorial(self):
        self.assertEqual(factorial.factorial(5), 120)

    def test_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("A man, a plan, a canal: Panama"))

    def test_file_word_count(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "sample.txt"
            path.write_text("hello world\npython", encoding="utf-8")
            result = files.file_word_count(path)
            self.assertEqual(result["words"], 3)

    def test_bank_account(self):
        account = bank.BankAccount("Test", 100)
        self.assertEqual(account.deposit(50), 150)
        self.assertEqual(account.withdraw(20), 130)

    def test_expenses(self):
        data = []
        expenses.add_expense(data, "Book", 25, "Study")
        self.assertEqual(expenses.total_expenses(data), 25)


if __name__ == "__main__":
    unittest.main()
