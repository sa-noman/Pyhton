import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "10-mini-projects"

def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative / "main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

number_guess = load("mini_number_guess", "01-number-guessing")
rps = load("mini_rps", "05-rock-paper-scissors")
pdfs = load("mini_pdfs", "06-compare-two-pdfs")
mastermind = load("mini_mastermind", "10-mastermind")
game2048 = load("mini_2048", "11-2048")
flames = load("mini_flames", "12-flames")
creature = load("mini_creature", "13-creature-training-game")
weather = load("mini_weather", "16-live-weather-notifications")
cows = load("mini_cows", "18-cows-and-bulls")
attendance = load("mini_attendance", "19-attendance-tracker")
higher = load("mini_higher", "20-higher-lower")
receipt = load("mini_receipt", "22-payment-receipt")

class MiniProjectTests(unittest.TestCase):
    def test_number_guessing_compare(self):
        self.assertEqual(number_guess.compare_guess(4, 5), "low")
        self.assertEqual(number_guess.compare_guess(6, 5), "high")
        self.assertEqual(number_guess.compare_guess(5, 5), "correct")

    def test_rps(self):
        self.assertEqual(rps.result("rock", "scissors"), "win")
        self.assertEqual(rps.result("rock", "rock"), "draw")

    def test_pdf_compare(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "a.pdf"
            b = Path(td) / "b.pdf"
            a.write_bytes(b"%PDF-demo")
            b.write_bytes(b"%PDF-demo")
            self.assertTrue(pdfs.identical(a, b))

    def test_mastermind(self):
        self.assertEqual(mastermind.score_guess("1234", "1243"), (2, 2))

    def test_2048_compress(self):
        self.assertEqual(game2048.compress([2, 0, 2, 4]), [4, 4, 0, 0])

    def test_flames(self):
        self.assertIsInstance(flames.flames_result("Alice", "Bob"), str)

    def test_creature_training(self):
        pet = creature.Creature("Spark")
        pet.train(25)
        self.assertEqual(pet.level, 2)

    def test_weather_format(self):
        text = weather.format_weather({"city":"Dhaka","temp_c":30,"summary":"clear sky"})
        self.assertIn("Dhaka", text)

    def test_cows_and_bulls(self):
        self.assertEqual(cows.score("1234", "1243"), (2, 2))

    def test_attendance(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "attendance.csv"
            attendance.mark_attendance(path, "Student", day="2026-09-30")
            self.assertIn("Student", path.read_text(encoding="utf-8"))

    def test_higher_lower(self):
        self.assertEqual(higher.compare(10, 20), "higher")
        self.assertEqual(higher.compare(20, 10), "lower")

    def test_receipt_total(self):
        item = receipt.Receipt("Book", 2, 50)
        self.assertEqual(item.total, 100)

if __name__ == "__main__":
    unittest.main()
