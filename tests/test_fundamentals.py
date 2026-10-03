import ast
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "Python Basic"


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PythonBasicStructureTests(unittest.TestCase):
    def test_required_categories_exist(self):
        required = {
            "Basics", "Strings", "Data Structures", "Control Flow", "Functions",
            "OOP", "Modules & Standard Library", "Errors & Files", "Python Tools",
        }
        self.assertTrue(required.issubset({p.name for p in BASIC.iterdir() if p.is_dir()}))

    def test_all_python_basic_files_parse(self):
        for path in BASIC.rglob("*.py"):
            with self.subTest(path=str(path.relative_to(ROOT))):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    def test_moved_projects_still_work(self):
        calculator = load("calculator", "23 mini project/Utilities/calculator.py")
        temperature = load("temperature", "23 mini project/Utilities/temperature_converter.py")
        leap = load("leap", "23 mini project/Beginner Practice/leap_year.py")
        prime = load("prime", "23 mini project/Utilities/prime_checker.py")
        self.assertEqual(calculator.calculate(4, 2, "*"), 8)
        self.assertAlmostEqual(temperature.celsius_to_fahrenheit(0), 32)
        self.assertTrue(leap.is_leap_year(2024))
        self.assertTrue(prime.is_prime(29))


if __name__ == "__main__":
    unittest.main()
