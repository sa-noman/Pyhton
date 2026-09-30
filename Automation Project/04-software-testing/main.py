"""Automatically discover and run unittest suites."""

from dataclasses import dataclass
from pathlib import Path
import argparse
import unittest


@dataclass
class TestSummary:
    tests_run: int
    failures: int
    errors: int
    skipped: int

    @property
    def passed(self) -> bool:
        return self.failures == 0 and self.errors == 0


def run_tests(directory: Path) -> TestSummary:
    suite = unittest.defaultTestLoader.discover(str(directory))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return TestSummary(
        tests_run=result.testsRun,
        failures=len(result.failures),
        errors=len(result.errors),
        skipped=len(result.skipped),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default="tests")
    args = parser.parse_args()

    summary = run_tests(Path(args.directory))
    print(summary)
    raise SystemExit(0 if summary.passed else 1)


if __name__ == "__main__":
    main()
