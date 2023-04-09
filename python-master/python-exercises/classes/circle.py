class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = 3.14 * self.radius ** 2
        area = round(area, 2)
        return area

    def getCircumference(self):
        circum = 2 * 3.14 * self.radius
        circum = round(circum, 2)
        return circum

    def compare(self, Circle1):
        if Circle1.getArea() >= self.getArea():
            return print(True)
        else:
            return print(False)


c1 = Circle(5)
print(c1.getArea())

class Circle1 (Circle) :
    def __init__(self, radius):
        self.radius = radius

c2 = Circle1(3)
print(c2.getArea())

c2.compare(c1)

#if __name__ == '__main__'






