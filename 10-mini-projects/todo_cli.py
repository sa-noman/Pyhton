import json
from pathlib import Path


def add_task(tasks: list[dict], text: str) -> None:
    tasks.append({"text": text.strip(), "done": False})


def complete_task(tasks: list[dict], index: int) -> None:
    if not 0 <= index < len(tasks):
        raise IndexError("Task index out of range.")
    tasks[index]["done"] = True


def save_tasks(tasks: list[dict], path: Path) -> None:
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def load_tasks(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    data_file = Path("tasks.json")
    tasks = load_tasks(data_file)
    add_task(tasks, input("New task: "))
    save_tasks(tasks, data_file)
    for i, task in enumerate(tasks, 1):
        mark = "✓" if task["done"] else " "
        print(f"{i}. [{mark}] {task['text']}")
