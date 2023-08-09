class Shapes:
    def __init__(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shapes):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Create instances of Circle and Rectangle
circle = Circle(7)
rectangle = Rectangle(6, 4)

# Calculate and print the areas
print("Area of the circle is:", circle.calculate_area())
print("Area of the rectangle is:", rectangle.calculate_area())
