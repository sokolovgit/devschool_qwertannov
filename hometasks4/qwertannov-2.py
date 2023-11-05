from math import sqrt


class Vector:

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def check_lengths(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise Exception

    def add(self, other):
        self.check_lengths(other)

        result = [a + b for a, b in zip(self.coordinates, other.coordinates)]

        return Vector(result)

    def subtract(self, other):
        self.check_lengths(other)

        result = [a - b for a, b in zip(self.coordinates, other.coordinates)]

        return Vector(result)

    def dot(self, other):
        self.check_lengths(other)

        return sum([a * b for a, b in zip(self.coordinates, other.coordinates)])

    def norm(self):
        return sqrt(sum([int(i) ** 2 for i in self.coordinates]))

    def equals(self, other):
        return all(a == b for a, b in zip(self.coordinates, other.coordinates))

    def __str__(self):
        return f"({','.join(map(str, self.coordinates))})"
