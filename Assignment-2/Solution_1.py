class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name is {self.name} and Age is {self.age}")


prs = Person('Ishaan', 20)
prs.show()
