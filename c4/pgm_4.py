class Rectangle:
    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def __lt__(self, other):
        return self.area() < other.area()

l1 = int(input("enter first length:"))
b1 = int(input("enter first bredth:"))

r1 = Rectangle(l1, b1)

l2 = int(input("enter second length:"))
b2 = int(input("enter second bredth:"))

r2 = Rectangle(l2, b2)


if r1 < r2:
    print("Rectangle r1 has smaller area than r2")
else:
    print("Rectangle r1 has greater or equal area than r2")
