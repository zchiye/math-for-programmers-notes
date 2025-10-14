class Vector:

    dimension = 2
    values = []

    def __init__(self, *values):
        if len(values) < 2:
            raise ValueError("A vector must have at least two dimensions.")
        self.dimension = len(values)
        self.values = list(values)

    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions must be the same for subtraction.")
        return Vector(*[a - b for a, b in zip(self.values, other.values)])
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only multiply by a scalar (int or float).")
        return Vector(*[a * scalar for a in self.values])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only divide by a scalar (int or float).")
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return Vector(*[a / scalar for a in self.values])
    
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.values))})"
    
    # def __str__(self):
    #     return f"({', '.join(map(str, self.values))})"
    
    def __eq__(self, value):
        return self.values == value.values
    
    def dot(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions must be the same for dot product.")
        return sum(a * b for a, b in zip(self.values, other.values))
    
    def add(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions must be the same for addition.")
        return Vector(*[a + b for a, b in zip(self.values, other.values)])

    def average(*vectors):
        if not vectors:
            raise ValueError("No vectors provided for average.")
        if len(vectors) == 1:
            return vectors[0]
        scalar = 1.0 / len(vectors)
        result = Vector(*[0,] * vectors[0].dimension)
        for v in vectors:
            result += v * scalar
        return result
    

if __name__ == "__main__":
    print(Vector.average(Vector(1,2,3), Vector(4,5,6)))
    print(Vector.average(Vector(1,2), Vector(4,5), Vector(3,6)))