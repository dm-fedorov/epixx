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

a = Point()
print (str (a))
b = Point (3,4)
print (str (b))
b.x = -19
print (a.func ())
print (str (b))
print (a == b, a != b)
