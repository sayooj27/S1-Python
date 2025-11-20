class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)




l1 = int(input("enter first length:"))
b1 = int(input("enter first bredth:"))

r1 = Rectangle(l1, b1)
l2 = int(input("enter second length:"))
b2 = int(input("enter second bredth:"))
r2 = Rectangle(l2, b2)
print("Area of r1:", r1.area())
print("perimeter",r1.perimeter())
print("Area of r2:", r2.area())
print("perimeter",r2.perimeter())

if r1.area()> r2.area():
    print("Rectangle r1 is larger by area.")
elif r1.area() < r2.area():
    print("Rectangle r2 is larger by area.")
else:
    print("Both rectangles have the same area.")
