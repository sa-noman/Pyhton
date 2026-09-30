# Python Fundamentals

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Programming%20Fundamentals-6C63FF)
![Tests](https://img.shields.io/badge/Tests-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

A structured collection of Python fundamentals, practice programs, and beginner-friendly mini projects. The repository grows from basic syntax to functions, data structures, file handling, object-oriented programming, error handling, and small command-line applications.

## Topics Covered

| Section | Concepts |
|---|---|
| 01 Basics | input/output, variables, arithmetic, type conversion |
| 02 Control Flow | conditions, loops, validation |
| 03 Data Structures | lists, dictionaries, sets |
| 04 Functions | reusable functions, recursion, algorithms |
| 05 Strings | text processing, palindrome checks, statistics |
| 06 File Handling | reading, writing, persistent notes |
| 07 OOP | classes, objects, methods, state |
| 08 Exceptions | safe input and error handling |
| 09 Standard Library | random, secrets, pathlib |
| 10 Mini Projects | 26 projects covering games, utilities, desktop tools, file tasks, and practical apps |
| Automation Project | 10 practical automation projects for messaging, testing, search, email, backup, and hotword detection |

## Repository Structure

```text
python-fundamentals/
├── 01-basics/
├── 02-control-flow/
├── 03-data-structures/
├── 04-functions/
├── 05-strings/
├── 06-file-handling/
├── 07-oop/
├── 08-exceptions/
├── 09-standard-library/
├── 10-mini-projects/
├── Automation Project/
│   ├── 01-instagram-messages/
│   ├── 02-facebook-birthday-post/
│   ├── 03-birthday-mail/
│   ├── 04-software-testing/
│   ├── 05-google-search/
│   ├── 06-linkedin-connections/
│   ├── 07-facebook-bulk-posting/
│   ├── 08-automated-email-messages/
│   ├── 09-automate-backup/
│   └── 10-hotword-detection/
├── tests/
├── .github/workflows/tests.yml
└── README.md
```

## Run a Program

```bash
python 01-basics/calculator.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Learning Goal

The goal of this repository is to build strong Python programming fundamentals through small, readable, testable programs before moving into larger automation and AI projects.

## Existing Early Exercises

The original `average.py` and `temperature.py` files are kept as early learning exercises and historical progress.


## Mini Projects

The `10-mini-projects` section now includes the original Expense Tracker, To-Do CLI, and Contact Book plus 23 independently implemented project ideas covering games, PDF comparison, emoji conversion, audio/screen tools, notifications, weather, attendance, receipts, timers, and more.

The earlier Number Guessing exercise was moved into this section instead of being duplicated. For the requested keylogger idea, the repository includes a safe foreground-only Keyboard Event Monitor rather than a system-wide keystroke logger.

See [10-mini-projects/README.md](./10-mini-projects/README.md) for the full list.

## Automation Projects

The `Automation Project` folder contains 10 independently implemented Python automation projects inspired by common real-world automation ideas. They cover social messaging workflows, birthday automation, automated software testing, browser search, email, backups, and hotword detection.

Social and messaging examples are designed with dry-run, explicit-send, manual-review, or managed-account controls so they can be studied safely without accidental posting or messaging.

See [Automation Project/README.md](./Automation%20Project/README.md) for the full project list and usage notes.
