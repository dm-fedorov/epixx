class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return "({0.x}, {0.y})".format(self)
    def func (self):
        return abs (self.x-self.y) 


class Circle (Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * self.radius
    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)
    def __str__(self):
        return "({0.radius}, {0.x}, {0.y})".format(self)

circle = Circle(2)

circle.radius = 3
circle.x = 12
a = Circle(4, 5, 6)
b = Circle(4, 5, 6)
print (str (a))
print (str (b))

print (a == b)
print (a == circle)
print (a != circle)

print (circle.func ())
