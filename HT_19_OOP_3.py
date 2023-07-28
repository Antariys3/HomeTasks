import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circle_length(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'Circle({self.x}, {self.y}, radius = {self.radius})'

    def __add__(self, other):
        new = super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, new.x, new.y)

    def __sub__(self, other):
        new_radius = abs(self.radius - other.radius)
        if new_radius == 0:
            return Point(self.x, self.y)
        else:
            return Circle(new_radius, self.x, self.y)


circle_1 = Circle(3, x=4, y=3)
circle_2 = Circle(5, x=5, y=2)
circle_3 = Circle(5, x=1, y=7)

print(circle_2 - circle_1)  # стандартный случай
print(circle_1 - circle_2)  # проверка модуля
print(circle_2 - circle_3)  # проверка на равенство
