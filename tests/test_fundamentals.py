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
    def test_required_concept_files_exist(self):
        required = {
            "syntax.py", "comments.py", "variables.py", "data_types.py", "numbers.py",
            "type_casting.py", "none.py", "strings.py", "booleans.py", "operators.py",
            "lists.py", "tuples.py", "sets.py", "dictionaries.py", "arrays.py",
            "conditionals.py", "while_loop.py", "for_loop.py", "functions.py",
            "function_arguments.py", "lambda.py", "recursion.py", "scope.py",
            "decorators.py", "generators.py", "iterators.py", "modules.py", "dates.py",
            "math.py", "random_module.py", "json.py", "regex.py", "user_input.py",
            "exceptions.py", "file_handling.py", "oop.py", "inheritance.py",
            "polymorphism.py", "encapsulation.py", "class_methods.py",
            "magic_methods.py", "inner_classes.py", "type_hints.py",
            "pip_and_packages.md", "virtual_environment.md", "README.md",
        }
        self.assertTrue(required.issubset({p.name for p in BASIC.iterdir()}))

    def test_all_python_basic_files_parse(self):
        for path in BASIC.glob("*.py"):
            with self.subTest(path=path.name):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    def test_old_numbered_folders_removed(self):
        for folder in [
            "01-basics", "02-control-flow", "03-data-structures", "04-functions",
            "05-strings", "06-file-handling", "07-oop", "08-exceptions",
            "09-standard-library",
        ]:
            self.assertFalse((ROOT / folder).exists())

    def test_moved_projects_still_work(self):
        calculator = load("calculator", "23 mini project/calculator.py")
        temperature = load("temperature", "23 mini project/temperature_converter.py")
        leap = load("leap", "23 mini project/leap_year.py")
        prime = load("prime", "23 mini project/prime_checker.py")
        self.assertEqual(calculator.calculate(4, 2, "*"), 8)
        self.assertAlmostEqual(temperature.celsius_to_fahrenheit(0), 32)
        self.assertTrue(leap.is_leap_year(2024))
        self.assertTrue(prime.is_prime(29))


if __name__ == "__main__":
    unittest.main()
