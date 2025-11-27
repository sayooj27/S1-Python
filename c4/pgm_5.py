class Time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __add__(self, other):
        h = self.__hour + other.__hour
        m = self.__minute + other.__minute
        s = self.__second + other.__second

        if s >= 60:
            m += s // 60
            s = s % 60

        if m >= 60:
            h += m // 60
            m = m % 60

        t3 = Time(h, m, s)
        return t3

    def display(self):
        print("hour:minute:second")
        print(f"{self.__hour}:{self.__minute}:{self.__second}")


print("Enter Time 1")
h1 = int(input("Hour: "))
m1 = int(input("Minute: "))
s1 = int(input("Second: "))
t1 = Time(h1, m1, s1)
print("\nEnter Time 2")
h2 = int(input("Hour: "))
m2 = int(input("Minute: "))
s2 = int(input("Second: "))
t2 = Time(h2, m2, s2)
print("\nTime 1: ", end="")
t1.display()
print("Time 2: ", end="")
t2.display()
t3 = t1 + t2
print("Sum of Time 1 and Time 2: ", end="")
t3.display()