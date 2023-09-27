class Figure:

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius


    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getPerimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b

    def getPerimeter(self):
        return 2 * (self.a + self.b)


def showPerimeter(figure):
    print(figure.getPerimeter())


def showArea(figure):
    print(figure.getArea())

circle = Circle(4)
rectangle = Rectangle(2, 6)


showPerimeter(circle)
showPerimeter(rectangle)

showArea(circle)
showArea(rectangle)

