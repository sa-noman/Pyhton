"""Nested / inner classes."""
class Computer:
    class CPU:
        def info(self):
            return "CPU"
    def __init__(self):
        self.cpu = self.CPU()
computer = Computer()
print(computer.cpu.info())
