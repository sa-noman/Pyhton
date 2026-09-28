class Student:
    def __init__(self, name: str, marks: list[float]) -> None:
        self.name = name
        self.marks = marks

    @property
    def average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def summary(self) -> str:
        return f"{self.name}: average={self.average:.2f}"


if __name__ == "__main__":
    student = Student("Noman", [78, 84, 91])
    print(student.summary())
