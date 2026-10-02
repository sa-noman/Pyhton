"""Instance, class, and static methods."""
class Converter:
    factor = 1000
    @classmethod
    def kilometers_to_meters(cls, km):
        return km * cls.factor
    @staticmethod
    def is_positive(value):
        return value > 0
print(Converter.kilometers_to_meters(2))
print(Converter.is_positive(5))
