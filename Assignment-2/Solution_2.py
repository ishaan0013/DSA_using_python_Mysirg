class Circle:
    def __init__(self):
        self._radius = 0

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, a):
        if (a < 0):
            raise ValueError("Invalid")
        self._radius = a

    def GetArea(self):
        area = (22/7)*self.radius**2
        print(f"Area is {area}")

    def GetCircumference(self):
        cir = 2*(22/7)*self.radius
        print(f"Circumference is {cir}")


c1 = Circle()
c1.radius = -1
c1.GetArea()
