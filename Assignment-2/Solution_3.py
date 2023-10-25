class Rectangle:
    length, breadth = None, None

    def SetDimensions(self, len, bth):
        self.length = len
        self.breadth = bth

    def ShowDimensions(self):
        print(f"Length is {self.length} and Breadth is {self.breadth}")

    def GetArea(self):
        print("Area is "+str(self.length*self.breadth))


rec = Rectangle()
rec.SetDimensions(10, 20)
rec.ShowDimensions()
rec.GetArea()
