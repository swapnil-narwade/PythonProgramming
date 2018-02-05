class Circle(object):
    pi = 3.143

    def __init__(self, ra):
        self.radius = ra

    def area(self):
        area1 = self.pi * (self.radius**2)
        return area1


c1 = Circle(ra = 300)
print(c1.area())
