import math


class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        # self.r - не аттрибут, а ссылка на @r.setter
        self.r = r

    def length(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return "Окружность ({0.x}; {0.y}) радиус = {0.r}".format(self)

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        assert r > 0, "Радиус должен быть положительным!"
        self._r = r


c = Circle(3, 4, 1)
# равносильно c.set_r(c.get_r() * 5)
c.r *= 5
print(c)
print(c.length(), c.square())
c.r = -1

