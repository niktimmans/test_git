

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point2D(self.x + other, self.y + other)
        else:
            raise TypeError('Нельзя сложить {1} к {0}'.format(self.__class__, type(other)))

    def __str__(self):
        return 'Точка 2Д ({}, {})'.format(self.x, self.y)

    @staticmethod
    def add(a, b):
        return Point2D(a.x + b.x, a.y + b.y)

point = Point2D(2, 3)
point2 = Point2D(5, 3)


print(Point2D.add(point, point2))

print(point + 4)

print(point + 'abcd')